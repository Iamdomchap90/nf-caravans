from django.db import models
from django.db.models import Q

from cms.models import CMSPlugin
from taggit.models import Tag

from case_studies.models import CaseStudy


class CaseStudyCardsPlugin(CMSPlugin):
    """
    Model for the Case Study card plugin
    """

    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(
        to=Tag,
        blank=True,
        help_text="Limit case studies based on tags.",
    )

    def __str__(self):
        return f"Case Study cards: {self.title}"

    def copy_relations(self, oldinstance):
        """
        Copy the relations from oldinstance and update the plugin field
        """

        for item in oldinstance.plugin_case_studies.all():
            item.pk = None
            item.plugin = self
            item.save()

    @property
    def filter_query(self) -> Q:
        """
        Builds the Q query object to use for filtering case studies.
        """
        query = Q()

        if self.tags.exists():
            query |= Q(tags__in=self.tags.all())

        return query

    def get_case_studies(self):
        """
        Return a queryset based on what the user chooses on the frontend
        """
        queryset = CaseStudy.objects.published()

        if query := self.filter_query:
            queryset = queryset.filter(query)

        return queryset


class CaseStudyCard(models.Model):
    """
    A model for an individual CaseStudy card plugin
    """

    case_study = models.ForeignKey(
        to=CaseStudy,
        related_name="case_study_cards",
        verbose_name="Case Study",
        on_delete=models.CASCADE,
        limit_choices_to={"is_published": True},
    )

    plugin = models.ForeignKey(
        to=CaseStudyCardsPlugin,
        on_delete=models.CASCADE,
        related_name="plugin_case_studies",
    )

    def __str__(self):
        return f"Case Study card: {self.case_study}"
