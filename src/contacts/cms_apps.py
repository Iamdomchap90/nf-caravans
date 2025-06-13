from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class ContactApp(CMSApp):
    app_name = "contacts"
    name = "Contacts"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["contacts.urls"]
