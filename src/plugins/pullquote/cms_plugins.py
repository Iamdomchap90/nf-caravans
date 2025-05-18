from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.pullquote import models

__all__ = ["PullQuotePlugin"]


@plugin_pool.register_plugin
class PullQuotePlugin(CMSPluginBase):
    """
    Plugin base for pull quote model
    """

    model = models.PullQuote
    name = "Pull Quote"
    render_template = "plugins/pullquote.html"
