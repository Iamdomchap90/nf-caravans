from django.db import models
from django.urls import reverse

from filer.fields.image import FilerImageField

from core.mixins.models import TimestampMixin, URLMixin


class Category(TimestampMixin):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Person(TimestampMixin, URLMixin):
    """
    Represents a Person object
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField()
    position = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        to=Category, on_delete=models.SET_NULL, null=True, related_name="people"
    )
    image = FilerImageField(
        related_name="person_image", null=True, on_delete=models.SET_NULL, blank=True
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Set this to prioritise the order of the person, higher numbers are higher "
        "priority",
    )

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["-order", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("people:detail", kwargs={"slug": self.slug})
