from django.views.generic import DetailView

from core.mixins.forms import PeriodFilterForm
from core.mixins.views import FormFilterListView, PublishedMixin
from events.models import Event


class EventListView(PublishedMixin, FormFilterListView):
    """
    Index view for Event queryset
    """

    model = Event
    template_name = "events/index.html"
    paginate_by = 9
    form_class = PeriodFilterForm


class EventDetailView(PublishedMixin, DetailView):
    """
    Detail view for an Event object
    """

    model = Event
    template_name = "events/detail.html"
