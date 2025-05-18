from django.db import models
from django.db.models import Q

from cms.models import CMSPlugin
from taggit.models import Tag

from events.models import Event


class EventCardsPlugin(CMSPlugin):
    """
    Model for the related event card plugin
    """

    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(
        to=Tag,
        limit_choices_to={"events__isnull": False},
        blank=True,
        help_text="Limit events based on tags.",
    )

    def __str__(self):
        return f"Event cards: {self.title}"

    def copy_relations(self, oldinstance):
        """
        Copy the relations from oldinstance and update the plugin field
        """

        for item in oldinstance.plugin_events.all():
            item.pk = None
            item.plugin = self
            item.save()

    @property
    def filter_query(self) -> Q:
        """
        Builds the Q query object to use for filtering events.
        """
        query = Q()

        if self.tags.exists():
            query |= Q(tags__in=self.tags.all())

        return query

    def get_events(self):
        """
        Return a queryset based on what the user chooses on the frontend
        """
        queryset = Event.objects.published()

        if query := self.filter_query:
            queryset = queryset.filter(query)

        return queryset


class EventCard(models.Model):
    """
    A model for an individual event card plugin
    """

    event = models.ForeignKey(
        to=Event,
        related_name="event_cards",
        verbose_name="Event",
        on_delete=models.CASCADE,
        limit_choices_to={"is_published": True},
    )

    plugin = models.ForeignKey(
        to=EventCardsPlugin,
        on_delete=models.CASCADE,
        related_name="plugin_events",
    )

    def __str__(self):
        return f"Event card: {self.event}"
