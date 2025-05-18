from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from core.mixins.models import VideoURLMixin


class Video(CMSPlugin, VideoURLMixin):
    """
    Represents a Video object
    """

    image = FilerImageField(on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=128)
    alt_text = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f"Video: {self.title}"
