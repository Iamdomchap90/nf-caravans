from django.urls import path

from events.views import EventDetailView, EventListView

app_name = "events"

urlpatterns = [
    path("", EventListView.as_view(), name="index"),
    path("<slug:slug>/", EventDetailView.as_view(), name="detail"),
]
