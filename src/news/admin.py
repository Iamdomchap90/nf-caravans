from django.contrib import admin

from core.mixins import admin as admin_mixins
from news.models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_filter = ["tags"]
    autocomplete_fields = ["author"]
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
