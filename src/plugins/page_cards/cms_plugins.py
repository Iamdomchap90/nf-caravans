from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models

__all__ = ["PageCardBlockPlugin", "PageCardPlugin"]


@plugin_pool.register_plugin
class PageCardBlockPlugin(CMSPluginBase):
    """
    Plugin for the page card block model
    """

    model = models.PageCardBlock
    name = "Page Cards Block"
    render_template = "plugins/page_cards/container.html"
    allow_children = True
    child_classes = ["PageCardPlugin"]


@plugin_pool.register_plugin
class PageCardPlugin(CMSPluginBase):
    """
    Plugin for page card model
    """

    model = models.PageCard
    name = "Page Card"
    render_template = "plugins/page_cards/item.html"
    require_parent = True
    parent_class = ["PageCardBlockPlugin"]
    fieldsets = [
        (None, {"fields": ["image"]}),
        ("Text", {"fields": ["title", "summary"]}),
        (
            "CTA",
            {
                "fields": [
                    "internal_link",
                    "external_url",
                    "cta_text",
                    "new_tab",
                ]
            },
        ),
    ]
