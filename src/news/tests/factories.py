import factory

from core.tests.factories import CategoryFactoryMixin, ContentModelFactoryMixin
from news.models import Article, Category


class CategoryFactory(CategoryFactoryMixin):
    class Meta:
        model = Category


class ArticleFactory(ContentModelFactoryMixin):
    title = factory.Faker("word")
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory("people.tests.factories.PersonFactory")

    class Meta:
        model = Article
