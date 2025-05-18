from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.event_cards.models import EventCard, EventCardsPlugin


class EventInline(admin.TabularInline):
    model = EventCard
    autocomplete_fields = ["event"]
    max_num = 5
    extra = 1
    fk_name = "plugin"


@plugin_pool.register_plugin
class EventCardsContainerPlugin(CMSPluginBase):
    model = EventCardsPlugin
    name = "Event Cards"
    render_template = "plugins/event_cards.html"
    inlines = [EventInline]
    filter_horizontal = ["tags"]

    def render(self, context, instance, placeholder):
        """
        Override the default render to allow the user to set a custom number of
        events to be shown
        """
        context = super().render(context, instance, placeholder)
        events = instance.get_events()
        current_event = context.get("event")

        if current_event:
            events = events.exclude(pk=current_event.pk)

        context.update({"events": events[:3]})
        return context
