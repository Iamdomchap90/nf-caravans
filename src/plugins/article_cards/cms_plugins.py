from django.contrib import admin

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from plugins.article_cards.models import ArticleCard, ArticleCardsPlugin


class ArticleInline(admin.TabularInline):
    model = ArticleCard
    autocomplete_fields = ["article"]
    max_num = 5
    extra = 1
    fk_name = "plugin"


@plugin_pool.register_plugin
class ArticleCardsContainerPlugin(CMSPluginBase):
    model = ArticleCardsPlugin
    name = "Article Cards"
    render_template = "plugins/article_cards.html"
    inlines = [ArticleInline]
    filter_horizontal = ["tags"]

    def render(self, context, instance, placeholder):
        """
        Override the default render to allow the user to set a custom number of
        articles to be shown
        """

        context = super().render(context, instance, placeholder)
        articles = instance.get_articles()
        current_article = context.get("article")

        if current_article:
            articles = articles.exclude(pk=current_article.pk)

        if selected_article_cards := instance.plugin_cards.all():
            articles = [card.article for card in selected_article_cards]

        context.update({"articles": articles[: instance.article_count]})
        return context
