from django.urls import path

from .views import ContactEnquirySuccessView, ContactEnquiryView

app_name = "contacts"

urlpatterns = [
    path("", ContactEnquiryView.as_view(), name="enquiry"),
    path("success/", ContactEnquirySuccessView.as_view(), name="success"),
]
