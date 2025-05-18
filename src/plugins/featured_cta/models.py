from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from core.mixins.models import URLMixin

__all__ = ["FeaturedCTA"]


class FeaturedCTA(CMSPlugin, URLMixin):
    """
    Model for the featured cta plugin
    """

    title = models.CharField(max_length=255)
    image = FilerImageField(on_delete=models.SET_NULL, null=True)
    description = models.TextField(blank=True)
    cta_text = models.CharField(max_length=255)

    def __str__(self):
        return f"Featured CTA: {self.title}"
