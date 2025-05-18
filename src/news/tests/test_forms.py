import pytest
from taggit.models import Tag

from news.forms import ArticleFilterForm
from news.models import Article
from news.tests.factories import ArticleFactory, CategoryFactory

pytestmark = pytest.mark.django_db


class TestArticleFilterForm:
    @pytest.fixture(autouse=True)
    def articles(self):
        return ArticleFactory.create_batch(3)

    @pytest.fixture
    def category(self):
        return CategoryFactory()

    @pytest.fixture
    def tag(self):
        return Tag.objects.create(name="alpha")

    def test_filter_queryset_tags(self, articles, tag):
        expected_article = ArticleFactory(tags=[tag])

        form = ArticleFilterForm(data={"tags": [tag]})
        form.is_valid()

        filtered_queryset = form.filter_queryset(Article.objects.all())

        assert len(filtered_queryset) == 1
        assert expected_article in filtered_queryset

    def test_filter_queryset_category(self, articles, category):
        expected_article = ArticleFactory(category=category)

        form = ArticleFilterForm(data={"categories": [category.pk]})

        form.is_valid()

        filtered_queryset = form.filter_queryset(Article.objects.all())

        assert len(filtered_queryset) == 1
        assert expected_article in filtered_queryset
