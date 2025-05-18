from django.db import models

from core.mixins.models import TimestampMixin


class FooterLinkQuerySet(models.QuerySet):
    """
    Custom queryset class for the Link class
    """

    def enabled(self):
        """
        Shows only the Link objects with is_enabled=True
        """
        return self.filter(is_enabled=True)


class FooterLink(TimestampMixin):
    """
    Represents a link in the footer
    """

    text = models.CharField(max_length=255)
    url = models.URLField()
    new_tab = models.BooleanField(default=False, help_text="Open this link in a new tab/window.")
    order = models.PositiveIntegerField(
        default=0,
        help_text="Set to prioritise the order of this link, higher numbers are shown first.",
    )
    is_enabled = models.BooleanField(
        default=False, help_text="Check this if you would like to display this link in the footer."
    )

    objects = FooterLinkQuerySet.as_manager()

    class Meta:
        ordering = ["-order", "text", "-created_at"]

    def __str__(self) -> str:
        return self.text
