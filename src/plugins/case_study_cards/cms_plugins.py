from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.case_study_cards.models import CaseStudyCard, CaseStudyCardsPlugin


class CaseStudyInline(admin.TabularInline):
    model = CaseStudyCard
    autocomplete_fields = ["case_study"]
    max_num = 5
    extra = 1
    fk_name = "plugin"


@plugin_pool.register_plugin
class CaseStudyCardsContainerPlugin(CMSPluginBase):
    model = CaseStudyCardsPlugin
    name = "Case Study Cards"
    render_template = "plugins/case_study_cards.html"
    inlines = [CaseStudyInline]
    filter_horizontal = ["tags"]

    def render(self, context, instance, placeholder):
        """
        Override the default render to allow the user to set a custom number of
        case_studies to be shown
        """
        context = super().render(context, instance, placeholder)
        case_studies = instance.get_case_studies()
        current_case_studies = context.get("case_study")

        if current_case_studies:
            case_studies = case_studies.exclude(pk=current_case_studies.pk)

        context.update({"case_studies": case_studies[:3]})
        return context
