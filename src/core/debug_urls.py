"""
A collection of urls that should only be viewable when DEBUG=True

Useful for debugging custom error pages
"""
from django.conf import settings
from django.urls import path
from django.views import defaults

urlpatterns = [
    path("500/", defaults.server_error),
    path(
        "403/",
        defaults.permission_denied,
        kwargs={"exception": Exception("Permission denied")},
    ),
    path(
        "404/",
        defaults.page_not_found,
        kwargs={"exception": Exception("Page not found")},
    ),
]
urlpatterns = urlpatterns if settings.DEBUG else []
