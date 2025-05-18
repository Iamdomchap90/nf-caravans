from django.views.generic import DetailView

from core.mixins.views import FormFilterListView, PublishedMixin
from news.forms import ArticleFilterForm
from news.models import Article


class ArticleIndex(PublishedMixin, FormFilterListView):
    """
    Index view for Article queryset
    """

    model = Article
    template_name = "news/index.html"
    paginate_by = 9
    form_class = ArticleFilterForm
    context_object_name = "articles"


class ArticleDetail(PublishedMixin, DetailView):
    """
    Detail view for an Article object.
    """

    model = Article
    template_name = "news/detail.html"
    context_object_name = "article"
