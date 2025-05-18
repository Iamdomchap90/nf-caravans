from django.contrib import admin

from core.mixins import admin as admin_mixins
from social_links import models


@admin.register(models.SocialLink)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["name", "url", "order", "is_enabled"]
    list_editable = ["order", "is_enabled"]
    list_filter = ["is_enabled"]
    search_fields = ["name"]
    fieldsets = [
        (
            None,
            {"fields": ["name", "url", "icon", "order", "is_enabled"]},
        ),
        admin_mixins.READONLY_FIELDSET,
    ]
    readonly_fields = admin_mixins.READONLY_FIELDS
