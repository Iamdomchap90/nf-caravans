from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import ContactEnquiryForm
from .models import Contact


class ContactEnquiryView(CreateView):
    model = Contact
    form_class = ContactEnquiryForm
    template_name = "contacts/form.html"
    success_url = reverse_lazy("contacts:success")


class ContactEnquirySuccessView(TemplateView):
    template_name = "contacts/success.html"
