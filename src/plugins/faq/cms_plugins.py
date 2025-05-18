from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.faq.models import FAQContainer


@plugin_pool.register_plugin
class FAQPlugin(CMSPluginBase):
    """
    Plugin displaying a block of chosen FAQs. The template will render all of the published FAQs
    for the chosen categories.
    """

    model = FAQContainer
    name = "FAQs"
    render_template = "plugins/faqs.html"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["categories"] = (
            instance.categories.all().order_by("-order").prefetch_related("faqs")
        )
        return context
