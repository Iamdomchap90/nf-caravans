from django.views.generic import DetailView

from case_studies.forms import CaseStudyFilterForm
from case_studies.models import CaseStudy
from core.mixins.views import FormFilterListView, PublishedMixin


class CaseStudyListView(PublishedMixin, FormFilterListView):
    """
    Index view for displaying the list of published Case Studies
    """

    model = CaseStudy
    template_name = "case_studies/index.html"
    context_object_name = "case_studies"
    paginate_by = 12
    form_class = CaseStudyFilterForm


class CaseStudyDetailView(PublishedMixin, DetailView):
    """
    Detail view for displaying a CaseStudy object
    """

    namespace = "case_studies"
    template_name = "case_studies/detail.html"
    model = CaseStudy
    context_object_name = "case_study"
