from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed


class DenyIndexMiddleware:
    """
    Set a X-Robot-Tag header to no-index.
    Robots.txt must be set to allow crawling for this to work.
    """

    def __init__(self, get_response):
        self.get_response = get_response

        if not settings.DEBUG:
            raise MiddlewareNotUsed("DenyIndexMiddleware not needed on live env")

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Robots-Tag"] = "noindex"
        return response
