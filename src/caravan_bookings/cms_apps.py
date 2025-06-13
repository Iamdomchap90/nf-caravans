from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
class CaravanBookingApp(CMSApp):
    app_name = "caravan_bookings"
    name = "Bookings"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["caravan_bookings.urls"]
