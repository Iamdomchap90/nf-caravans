import factory

from core.tests.factories import CategoryFactoryMixin, ContentModelFactoryMixin
from events.models import Category, Event


class CategoryFactory(CategoryFactoryMixin):
    class Meta:
        model = Category


class EventFactory(ContentModelFactoryMixin):
    title = factory.Faker("word")
    category = factory.SubFactory(CategoryFactory)
    location = factory.Faker("city")
    start_date = factory.Faker("date")
    end_date = factory.Faker("date")
    start_time = factory.Faker("time")
    end_time = factory.Faker("time")

    class Meta:
        model = Event
