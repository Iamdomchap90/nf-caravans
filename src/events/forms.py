from django import forms
from django.db.models import Q

from core.mixins.forms import TextTagFilterForm
from events.models import Category


class EventFilterForm(TextTagFilterForm):
    """
    Provides data/methods for form filtering.
    """

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.filter(events__isnull=False).distinct(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    def category_query(self):
        if categories := self.cleaned_data.get("categories"):
            self.query &= Q(category__in=categories)
        return self.query

    @property
    def filter_query(self) -> Q:
        super().filter_query
        return self.category_query()
