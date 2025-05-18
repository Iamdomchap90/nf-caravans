import factory

from core.tests.factories import CategoryFactoryMixin
from people.models import Category, Person


class CategoryFactory(CategoryFactoryMixin):
    class Meta:
        model = Category


class PersonFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("name")
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Person
