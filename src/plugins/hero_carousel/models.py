from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from core.mixins.models import URLMixin


class HeroCarousel(CMSPlugin):
    """
    Model for the Hero carousel plugin
    """

    def __str__(self):
        return f"Hero {self.pk}"

    def copy_relations(self, oldinstance):
        self.hero_images.all().delete()

        for image in oldinstance.hero_images.all():
            image.pk = None
            image.hero = self
            image.save()


class Image(URLMixin):
    """
    Stores an image to use with a Featured Hero plugin
    """

    title = models.CharField(max_length=255)
    strapline = models.CharField(max_length=140, blank=True)
    cta_text = models.CharField(max_length=48, blank=True)
    image = FilerImageField(on_delete=models.SET_NULL, null=True)
    hero = models.ForeignKey(to=HeroCarousel, on_delete=models.CASCADE, related_name="hero_images")

    def __str__(self):
        return f"Image {self.pk} for {self.hero}"
