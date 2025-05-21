from django.db import models
from django.db.models import Q

from cms.models import CMSPlugin
from news.models import Category
from taggit.models import Tag

from news.models import Article


class ArticleCardsPlugin(CMSPlugin):
    """
    Model for the related article card plugin
    """

    title = models.CharField(max_length=255)
    article_count = models.IntegerField(default=3)
    tags = models.ManyToManyField(
        to=Tag,
        limit_choices_to={"articles__isnull": False},
        blank=True,
        help_text="Limit articles based on tags.",
    )
    category = models.ForeignKey(
        to=Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Limit articles based on a category.",
    )

    def __str__(self):
        return f"Article cards: {self.title}"

    def copy_relations(self, oldinstance):
        """
        Copy the relations from oldinstance and update the plugin field
        """

        for item in oldinstance.plugin_cards.all():
            item.pk = None
            item.plugin = self
            item.save()

    @property
    def filter_query(self) -> Q:
        """
        Builds the Q query object to use for filtering articles.
        """
        query = Q()

        if self.category:
            query &= Q(category=self.category)
        if self.tags.exists():
            query &= Q(tags__in=self.tags.all())

        return query

    def get_articles(self):
        """
        Return a queryset based on what the user chooses on the frontend
        """
        queryset = Article.objects.published()

        if query := self.filter_query:
            queryset = queryset.filter(query)

        return queryset


class ArticleCard(models.Model):
    """
    A model for an individual article card plugin
    """

    article = models.ForeignKey(
        to=Article,
        related_name="article_cards",
        verbose_name="Article",
        on_delete=models.CASCADE,
        limit_choices_to={"is_published": True},
        null=True,
        blank=True,
    )

    plugin = models.ForeignKey(
        to=ArticleCardsPlugin,
        on_delete=models.CASCADE,
        related_name="plugin_cards",
    )

    def __str__(self):
        return f"Article card: {self.article}"
