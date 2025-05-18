from django.contrib import admin

from core.mixins.admin import PUBLISHING_FIELDSET, READONLY_FIELDS, READONLY_FIELDSET
from faqs import models


@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    """
    Admin class for editing FAQ objects
    """

    list_display = ["question", "category", "order", "is_published"]
    list_filter = ["category", "is_published"]
    list_editable = ["order"]
    search_fields = ["question"]
    readonly_fields = READONLY_FIELDS
    fieldsets = [
        ("Structured Data", {"fields": ["question", "answer", "category", "order"]}),
        PUBLISHING_FIELDSET,
        READONLY_FIELDSET,
    ]


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for editing FAQ category objects
    """

    list_display = ["name", "order"]
    list_editable = ["order"]
    search_fields = ["name"]
    field_set = [("Structured Data", {"fields": ["name", "order"]})]
