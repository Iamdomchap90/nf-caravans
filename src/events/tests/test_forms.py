import pytest

from events.forms import EventFilterForm
from events.models import Event
from events.tests.factories import CategoryFactory, EventFactory

pytestmark = pytest.mark.django_db


class TestEventFilterForm:
    @pytest.fixture(autouse=True)
    def events(self):
        return EventFactory.create_batch(3)

    @pytest.fixture
    def category(self):
        return CategoryFactory()

    def test_filter_queryset_category(self, events, category):
        expected_event = EventFactory(category=category)

        form = EventFilterForm(data={"categories": [category.pk]})

        form.is_valid()

        filtered_queryset = form.filter_queryset(Event.objects.all())

        assert len(filtered_queryset) == 1
        assert expected_event in filtered_queryset
