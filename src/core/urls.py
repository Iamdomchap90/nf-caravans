from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from cms.sitemaps import CMSSitemap
from news.sitemaps import ArticleSitemap

from . import views

sitemaps = {
    "cms": CMSSitemap,
    "articles": ArticleSitemap,
}


urlpatterns = (
    [
        path("favicon.ico", views.favicon),
        path("robots.txt", views.robots),
        path("google33b1735040ebbe58.html", views.google_verification),
        path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
        path("sitemap/", views.sitemap, name="html_sitemap"),
        path("taggit_autosuggest/", include("taggit_autosuggest.urls")),
        path("accounts/", include("users.urls")),
        path("admin/", admin.site.urls),
        path("", include("cms.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

admin.site.site_header = "NF caravans"
admin.site.site_title = "NF caravans"
