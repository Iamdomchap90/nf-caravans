from datetime import datetime

from django.db import models
from django.urls import reverse

from cms.models import PlaceholderField
from filer.fields.image import FilerImageField
from giant_search.mixins import SearchableMixin
from taggit_autosuggest.managers import TaggableManager

from core.mixins.models import MetaMixin, PublishingMixin, PublishingQuerySetMixin, TimestampMixin


class Category(TimestampMixin):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


def default_start_time():
    now = datetime.now()
    return now.replace(hour=0, minute=0, second=0, microsecond=0)


class Event(TimestampMixin, PublishingMixin, MetaMixin, SearchableMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    image = FilerImageField(
        related_name="events",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    start_time = models.TimeField(default=default_start_time)
    start_date = models.DateField()
    end_time = models.TimeField(default=default_start_time)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)

    content = PlaceholderField(slotname="event_content", related_name="events")

    category = models.ForeignKey(
        to=Category, null=True, on_delete=models.SET_NULL, related_name="events"
    )
    tags = TaggableManager(related_name="events")

    objects = PublishingQuerySetMixin.as_manager()

    class Meta:
        ordering = ["-start_date", "start_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events:detail", kwargs={"slug": self.slug})

    @classmethod
    def get_search_queryset(cls):
        return cls.objects.published()

    def get_search_result_description(self):
        return self.description

    @property
    def time_display(self):
        display = (
            f"{self.start_date.strftime('%B %d, %Y')} at "
            f"{self.start_time.strftime('%I:%M %p')}"
        )

        if self.end_date:
            if self.end_date == self.start_date:
                display += f" - {self.end_time.strftime('%I:%M %p')}"
            else:
                display += (
                    f" to {self.end_date.strftime('%B %d, %Y')} at "
                    f"{self.end_time.strftime('%I:%M %p')}"
                )
        elif self.end_time != self.start_time:
            display += f" - {self.end_time.strftime('%I:%M %p')}"

        return display
