from django.urls import path

from .views import BookingEnquiryCreateView, BookingEnquirySuccessView

app_name = "caravan_bookings"

urlpatterns = [
    path("", BookingEnquiryCreateView.as_view(), name="booking_enquiry"),
    path("success/", BookingEnquirySuccessView.as_view(), name="success"),
]
