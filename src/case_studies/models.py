from django.db import models
from django.urls import reverse

from cms.models import PlaceholderField
from filer.fields.image import FilerImageField
from giant_search.mixins import SearchableMixin
from taggit_autosuggest.managers import TaggableManager

from core.mixins.models import MetaMixin, PublishingMixin, PublishingQuerySetMixin, TimestampMixin


class Category(TimestampMixin):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"

    def __str__(self):
        return self.name


class CaseStudy(SearchableMixin, TimestampMixin, PublishingMixin, MetaMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True)
    tags = TaggableManager(related_name="case_studies")
    description = models.TextField()
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    content = PlaceholderField(slotname="case_study_content")

    objects = PublishingQuerySetMixin.as_manager()

    class Meta:
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"
        ordering = ["-publish_at", "-updated_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("case_studies:detail", kwargs={"slug": self.slug})

    @classmethod
    def get_search_queryset(cls):
        return cls.objects.published()

    def get_search_result_description(self):
        return self.description
