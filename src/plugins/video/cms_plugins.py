from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models

__all__ = ["ContentWidthVideoPlugin"]


@plugin_pool.register_plugin
class ContentWidthVideoPlugin(CMSPluginBase):
    name = "Video"
    model = models.Video
    render_template = "plugins/video.html"
