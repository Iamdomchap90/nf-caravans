from django.db import models

from cms.models import CMSPlugin


class KeyStatisticContainer(CMSPlugin):
    """
    Represents a container that shows a row of Statistic objects
    """

    title = models.CharField(max_length=255)
    introduction = models.TextField(blank=True)

    def __str__(self):
        return f"Key statistic container {self.title}"

    def copy_relations(self, oldinstance):
        self.plugin_statistics.all().delete()

        for plugin_statistics in oldinstance.plugin_statistics.all():
            plugin_statistics.pk = None
            plugin_statistics.plugin = self
            plugin_statistics.save()


class Statistic(models.Model):
    """
    A statistic that is linked to a container model
    """

    stat_value = models.CharField(max_length=50)
    strapline = models.CharField(max_length=255)
    plugin = models.ForeignKey(
        KeyStatisticContainer,
        related_name="plugin_statistics",
        on_delete=models.SET_NULL,
        null=True,
    )

    @property
    def is_number(self):
        # Check if the value can be converted to a float or not
        try:
            float(self.stat_value)
        except ValueError:
            return False

        return True

    @property
    def decimal_places(self):
        # If the value can be converted to a float and contains a decimal point
        if self.is_number and "." in self.stat_value:
            # Return 2 if the value contains more than one decimal place
            if len(self.stat_value.split(".")[1]) > 1:
                return 2

            # Otherwise return 1
            return 1

        return 0

    def __str__(self):
        return f"Statistic {self.pk}"
