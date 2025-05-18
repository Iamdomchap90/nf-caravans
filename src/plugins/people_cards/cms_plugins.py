from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from people.models import Person
from plugins.people_cards import models


class PersonCardInline(admin.TabularInline):
    """
    People selection inline.
    """

    model = models.PersonCard
    extra = 1


@plugin_pool.register_plugin
class PersonContainerPlugin(CMSPluginBase):
    """
    Plugin for the PersonContainer plugin.
    """

    render_template = "plugins/people.html"
    name = "People Block"
    model = models.PersonContainer

    inlines = [PersonCardInline]

    def get_people(self, instance):
        """
        Get the people for this plugin instance. If a category is selected then return all Person
        objects for that category, or show the People objects assigned to this plugin instance.
        """
        if instance.category:
            return Person.objects.filter(category=instance.category)

        ids = instance.people_cards.all().values_list("person_id", flat=True)
        return Person.objects.filter(id__in=ids)

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context.update(
            {
                "people": self.get_people(instance),
            }
        )
        return context
