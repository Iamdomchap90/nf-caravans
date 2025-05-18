from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models

__all__ = ["IframeEmbedPlugin"]


@plugin_pool.register_plugin
class IframeEmbedPlugin(CMSPluginBase):
    """
    Plugin for an iframe embed
    """

    model = models.IframeEmbed
    name = "Iframe Embed"
    render_template = "plugins/iframe_embed.html"
