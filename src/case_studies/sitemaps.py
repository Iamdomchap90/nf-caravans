from django.contrib.sitemaps import Sitemap

from case_studies.models import CaseStudy


class CaseStudySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        """
        Get all active case studies
        """
        return CaseStudy.objects.published()

    def lastmod(self, obj):
        return obj.updated_at
