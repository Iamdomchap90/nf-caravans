from django.db import models

from core.fields import RichTextField
from core.mixins.models import PublishingMixin, PublishingQuerySetMixin, TimestampMixin


class FAQ(TimestampMixin, PublishingMixin):
    """
    A single question/answer pair.
    """

    question = models.CharField(max_length=255)
    answer = RichTextField()
    category = models.ForeignKey(
        to="faqs.Category", related_name="faqs", on_delete=models.SET_NULL, null=True
    )
    order = models.PositiveIntegerField(
        default=0, help_text="Higher number means a higher priority in listing."
    )

    objects = PublishingQuerySetMixin.as_manager()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ["-order", "question"]

    def __str__(self):
        if len(self.question) > 30:
            return self.question[:30] + "..."
        return self.question


class Category(models.Model):
    """
    Model for storing a FAQ Category in the database
    """

    name = models.CharField(max_length=255)
    order = models.PositiveIntegerField(
        default=0, help_text="Higher number means a higher priority in listing."
    )

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["-order", "name"]

    def __str__(self):
        return self.name

    @property
    def published_faqs(self):
        """
        Of the FAQs in this category, return only the published ones.
        """
        return self.faqs.published()
