from django.db import models

from cms.models import CMSPlugin

from people.models import Person


class PersonContainer(CMSPlugin):
    """
    Represents a selection of people relevant to the page.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        to="people.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="If set, only people in this category will be shown.",
    )

    def copy_relations(self, oldinstance):
        """
        Copy the relations from oldinstance and update the plugin field
        """
        self.people_cards.all().delete()
        for item in oldinstance.people_cards.all():
            item.pk = None
            item.plugin = self
            item.save()

    def __str__(self):
        return self.title


class PersonCard(models.Model):
    """
    Acts as a bridge between the people app and the people container plugin to allow for custom
    ordering
    """

    person = models.ForeignKey(to=Person, related_name="people_cards", on_delete=models.CASCADE)
    plugin = models.ForeignKey(
        to=PersonContainer, on_delete=models.CASCADE, related_name="people_cards"
    )

    def __str__(self):
        return f"Person card for {self.person.name}"
