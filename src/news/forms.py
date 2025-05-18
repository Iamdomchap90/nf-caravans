from django import forms
from django.db.models import Q

from core.mixins.forms import TextTagFilterForm
from news.models import Category


class ArticleFilterForm(TextTagFilterForm):
    """
    Form to provide search filtering for articles.
    """

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.filter(articles__isnull=False).distinct(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    def text_query(self):
        if text := self.cleaned_data.get("text"):
            self.query |= (
                Q(title__icontains=text)
                | Q(intro__icontains=text)
                | Q(plugin_text__icontains=text)
            )
        return self.query

    def category_query(self):
        if categories := self.cleaned_data.get("categories"):
            self.query &= Q(category__in=categories)
        return self.query

    @property
    def filter_query(self) -> Q:
        super().filter_query
        return self.category_query()
