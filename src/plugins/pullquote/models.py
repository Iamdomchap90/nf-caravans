from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class PullQuote(CMSPlugin):
    quote = models.TextField()
    citation = models.CharField(max_length=255, blank=True)
    citation_url = models.URLField(blank=True)
    image = FilerImageField(
        related_name="+",
        blank=True,
        null=True,
        help_text="Choose an optional image",
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"Pull quote {self.pk}"
