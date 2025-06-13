from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import RichTextForm
from .models import RichText

__all__ = ["RichTextPlugin"]


@plugin_pool.register_plugin
class RichTextPlugin(CMSPluginBase):
    """
    Rich text plugin
    """

    name = "Rich Text"
    model = RichText
    form = RichTextForm
    render_template = "plugins/rich_text.html"

    class Media:
        js = (
            "https://cdn.ckeditor.com/ckeditor5/40.0.1/classic/ckeditor.js",
            "frontend/js/init-ckeditor.js",
        )
