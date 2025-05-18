from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from newsletter.views import submit_newsletter

sitemaps = {}

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("vacancies/", include("vacancies.urls")),
    path("news/", include("news.urls")),
    path("newsletter/", submit_newsletter, name="newsletter_submit"),
    path("events/", include("events.urls")),
    path("forms/", include("forms.urls")),
    path("admin/", admin.site.urls),
    path("", include("cms.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
