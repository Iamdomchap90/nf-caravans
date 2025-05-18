from django.contrib import admin

from core.mixins import admin as admin_mixins
from events.models import Category, Event


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = admin_mixins.READONLY_FIELDS
    fieldsets = [
        (
            "Structured Data",
            {
                "fields": [
                    "name",
                    "slug",
                ]
            },
        ),
        admin_mixins.READONLY_FIELDSET,
    ]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "start_date", "end_date", "category", "is_published"]
    list_filter = ["category", "is_published"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = admin_mixins.READONLY_FIELDS
    filter_horizontal = ["tags"]
    fieldsets = [
        (
            "Structured Data",
            {
                "fields": [
                    "title",
                    "slug",
                    "description",
                    "image",
                    "location",
                    "category",
                    "tags",
                ]
            },
        ),
        (
            "Dates",
            {
                "fields": [
                    ("start_date", "start_time"),
                    ("end_date", "end_time"),
                ]
            },
        ),
        admin_mixins.META_FIELDSET,
        admin_mixins.PUBLISHING_FIELDSET,
        admin_mixins.READONLY_FIELDSET,
    ]
