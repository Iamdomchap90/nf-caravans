from django.contrib import admin

from case_studies.models import CaseStudy, Category
from core.mixins import admin as admin_mixins


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


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "is_published"]
    list_filter = ["category", "is_published"]
    search_fields = [
        "title",
    ]
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
                    "category",
                    "tags",
                    "description",
                    "image",
                ]
            },
        ),
        admin_mixins.META_FIELDSET,
        admin_mixins.PUBLISHING_FIELDSET,
        admin_mixins.READONLY_FIELDSET,
    ]
