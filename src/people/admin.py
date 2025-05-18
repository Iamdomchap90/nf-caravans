from django.contrib import admin

from core.mixins import admin as admin_mixins
from people.models import Category, Person


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


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "position", "category", "order"]
    search_fields = ["name", "position"]
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ["category"]
    list_editable = ["order"]
    readonly_fields = admin_mixins.READONLY_FIELDS
    fieldsets = (
        (
            "Structured Data",
            {
                "fields": [
                    "name",
                    "slug",
                    "position",
                    "category",
                    "order",
                    "image",
                    "description",
                    "internal_link",
                    "external_url",
                ]
            },
        ),
        admin_mixins.READONLY_FIELDSET,
    )
