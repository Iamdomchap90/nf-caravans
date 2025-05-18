from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class CaseStudiesApp(CMSApp):
    """
    App hook for Case studies app
    """

    app_name = "case_studies"
    name = "Case Studies"

    def get_urls(self, page=None, language=None, **kwargs):
        """
        Return the path to the apps urls module
        """

        return ["case_studies.urls"]
