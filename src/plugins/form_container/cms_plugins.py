from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Form


@plugin_pool.register_plugin
class FormContainerPlugin(CMSPluginBase):
    """
    Plugin for rendering a Form.
    """

    render_template = "plugins/form_container.html"
    name = "Form"
    model = Form
    module = "Forms"

    def __str__(self):
        return f"Form container {self.pk}"

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        form = instance.form.form_class()
        context.update({"form": form})
        return context
