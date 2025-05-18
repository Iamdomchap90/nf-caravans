from django.contrib import admin

from cms.extensions import PageExtensionAdmin

from .models import IndexExtension


@admin.register(IndexExtension)
class IndexExtensionAdmin(PageExtensionAdmin):
    pass
