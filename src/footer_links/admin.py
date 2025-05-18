from django.contrib import admin

from core.mixins import admin as admin_mixins
from footer_links import models


@admin.register(models.FooterLink)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["text", "url", "order", "is_enabled", "new_tab"]
    list_editable = ["order", "is_enabled", "new_tab"]
    list_filter = ["is_enabled"]
    search_fields = ["text"]
    fieldsets = [
        (
            None,
            {"fields": ["text", "url", "new_tab", "order", "is_enabled"]},
        ),
        admin_mixins.READONLY_FIELDSET,
    ]
    readonly_fields = admin_mixins.READONLY_FIELDS
