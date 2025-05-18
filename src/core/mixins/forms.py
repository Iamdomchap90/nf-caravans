from datetime import timedelta

from django import forms
from django.db.models import Q
from django.utils import timezone

from taggit.models import Tag


class TextFilterForm(forms.Form):
    """
    Provides methods for filtering via text. This will match against the name and description
    fields. If you want to filter by other fields, you'll need to override the filter_by_text
    method.
    """

    _query = None
    text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by title or keyword",
                "title": "Search",
            }
        ),
        required=False,
    )

    @property
    def query(self):
        return self._query or Q()

    @query.setter
    def query(self, value):
        self._query = value

    def text_query(self):
        if text := self.cleaned_data.get("text"):
            self.query &= Q(title__icontains=text) | Q(description__icontains=text)
        return self.query

    @property
    def filter_query(self) -> Q:
        return self.text_query()

    def filter_queryset(self, queryset):
        """
        Runs the queryset through several filters/sorting and returns the filtered queryset.
        """
        if not hasattr(self, "cleaned_data"):
            return queryset

        return queryset.filter(self.filter_query)


class TextTagFilterForm(TextFilterForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    def tags_query(self):
        """
        Filter the queryset based on tags and search query
        """
        if tags := self.cleaned_data.get("tags"):
            self.query &= Q(tags__in=tags)

        return self.query

    @property
    def filter_query(self) -> Q:
        self.tags_query()
        return super().filter_query


PERIOD_CHOICES_DAYS = (
    ("", "Select date range", 0),
    ("month", "Within the next month", 30),
    ("3-months", "Within the next 3 months", 92),
    ("6-months", "Within the next 6 months", 185),
    ("year", "Within the next year", 365),
    ("", "All time", 0),
)

PERIOD_DAYS = dict((str(val), days) for val, _, days in PERIOD_CHOICES_DAYS)


class PeriodFilterForm(TextTagFilterForm):
    period = forms.ChoiceField(
        choices=[(val, label) for (val, label, _) in PERIOD_CHOICES_DAYS],
        required=False,
        widget=forms.Select,
    )

    def period_query(self):
        """
        A number-of-days approximation to the intended period filtering
        """
        if period := self.cleaned_data.get("period"):
            start = timezone.now()
            end = start + timedelta(days=PERIOD_DAYS[period])
            self.query &= (
                Q(start_date__gte=start) | (Q(end_date__gt=start) & Q(start_date__lt=start))
            ) & Q(start_date__lte=end)
            return self.query
        return None

    @property
    def filter_query(self):
        self.period_query()
        return super().filter_query
