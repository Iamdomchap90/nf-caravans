from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import BookingEnquiryForm
from .models import BookingEnquiry


class BookingEnquiryCreateView(CreateView):
    model = BookingEnquiry
    form_class = BookingEnquiryForm
    template_name = "caravan_bookings/form.html"
    success_url = reverse_lazy("caravan_bookings:success")


class BookingEnquirySuccessView(TemplateView):
    template_name = "caravan_bookings/success.html"
