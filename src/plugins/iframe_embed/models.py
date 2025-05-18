from django.db import models

from cms.models import CMSPlugin

__all__ = ["IframeEmbed"]


class IframeEmbed(CMSPlugin):
    """
    Model for the iframe embed plugin.
    """

    snippet = models.TextField()

    def __str__(self):
        return f"Iframe Embed {self.pk}"
