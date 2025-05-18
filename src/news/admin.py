from django.contrib import admin

from giant_news.admin import ArticleAdmin as BaseArticleAdmin, CategoryAdmin

from core.mixins import admin as admin_mixins
from news.models import Article, Category

admin.site.register(Category, CategoryAdmin)


@admin.register(Article)
class ArticleAdmin(BaseArticleAdmin):
    autocomplete_fields = ["author"]
    filter_horizontal = ["tags"]
    fieldsets = [
        (
            "Structured Data",
            {
                "fields": [
                    "title",
                    "slug",
                    "author",
                    "category",
                    "photo",
                    "intro",
                    "tags",
                ]
            },
        ),
        admin_mixins.PUBLISHING_FIELDSET,
        admin_mixins.META_FIELDSET,
        admin_mixins.READONLY_FIELDSET,
    ]
