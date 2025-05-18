from django.utils.translation import gettext_lazy as _

from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool

from .models import IndexExtension, SocialShareImageExtension


@toolbar_pool.register
class IndexExtensionToolbar(ExtensionToolbar):
    model = IndexExtension

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()

        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(
                    _("Toggle indexing"),
                    url=url,
                    disabled=not self.toolbar.edit_mode_active,
                    position=3,
                )


@toolbar_pool.register
class SocialShareImageExtensionToolbar(ExtensionToolbar):
    model = SocialShareImageExtension

    def populate(self):
        current_page_menu = self._setup_extension_toolbar()

        if current_page_menu:
            page_extension, url = self.get_page_extension_admin()
            if url:
                current_page_menu.add_modal_item(
                    _("Social Share Image"),
                    url=url,
                    disabled=not self.toolbar.edit_mode_active,
                    position=0,
                )
