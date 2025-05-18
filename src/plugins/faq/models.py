from django.db import models

from cms.models import CMSPlugin

from faqs.models import Category


class FAQContainer(CMSPlugin):
    """
    Represents a model object for a FAQ container
    """

    title = models.CharField(max_length=255, blank=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"FAQ Container: {self.title}"

    def copy_relations(self, oldinstance):
        self.categories.set(oldinstance.categories.all())
