from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.key_stat import models

__all__ = ["KeyStatPlugin"]


class InlineStatistic(admin.StackedInline):
    """
    The selectable statistics.
    """

    model = models.Statistic
    max_num = 3
    extra = 3


@plugin_pool.register_plugin
class KeyStatPlugin(CMSPluginBase):
    """
    Plugin base for Key statistics model
    """

    model = models.KeyStatisticContainer
    name = "Key Statistics"
    render_template = "plugins/key_stat.html"
    inlines = [InlineStatistic]
    fieldsets = [
        ("Text", {"fields": ["title", "introduction"]}),
    ]
