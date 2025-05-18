from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField

from core.mixins.models import URLMixin


class PageCardBlock(CMSPlugin):
    """
    Model for the page card block plugin
    """

    def __str__(self):
        return f"Page card container {self.pk}"


class PageCard(CMSPlugin, URLMixin):
    """
    A model for an individual page card
    """

    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=140, blank=True, help_text="Limited to 140 characters")
    image = FilerImageField(related_name="+", on_delete=models.SET_NULL, null=True, blank=False)
    cta_text = models.CharField(max_length=50, default="Read more")

    def __str__(self):
        _identifier = self.title or f"#{self.pk}"

        if self._page:
            page_title = self._page.get_page_title()
            if page_title:
                _identifier = page_title

        return f"Page Card for {_identifier}"

    @property
    def _page(self):
        """
        Return the internal page object associated with this PageCard
        """
        return self.internal_link

    @property
    def is_page_published(self):
        """
        Return the publish state of the Internal Page linked to this card.
        """
        if not self._page:
            return False

        return self._page.is_published(self._page.languages)
