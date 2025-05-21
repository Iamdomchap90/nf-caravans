from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import BookingEnquiry
from .forms import BookingEnquiryForm


class BookingEnquiryCreateView(CreateView):
    model = BookingEnquiry
    form_class = BookingEnquiryForm
    template_name = "caravan_bookings/form.html"
    success_url = reverse_lazy("caravan_bookings:success")


class BookingEnquirySuccessView(TemplateView):
    template_name = "caravan_bookings/success.html"



