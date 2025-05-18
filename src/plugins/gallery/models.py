from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class GalleryBlock(CMSPlugin):
    """
    Model for the Gallery block. Container class which allows for displaying multiple images in
    either a carousel or thumbnail format
    """

    class Display(models.TextChoices):
        CAROUSEL = "carousel"
        THUMBNAILS = "thumbnails"

    display = models.CharField(max_length=255, choices=Display.choices, default=Display.CAROUSEL)

    def __str__(self):
        return f"Gallery plugin {self.pk}"


class GalleryImage(CMSPlugin):
    """
    Holds an image and details for a gallery image item
    """

    image = FilerImageField(on_delete=models.SET_NULL, null=True)
    photo_credit = models.CharField(
        max_length=255, blank=True, help_text="This will only be displayed on the modal"
    )

    def __str__(self):
        return f"Gallery image {self.pk}"
