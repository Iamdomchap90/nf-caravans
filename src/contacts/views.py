from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Contact
from .forms import ContactEnquiryForm


class ContactEnquiryView(CreateView):
    model = Contact
    form_class = ContactEnquiryForm
    template_name = "contacts/form.html"
    success_url = reverse_lazy("contacts:success")


class ContactEnquirySuccessView(TemplateView):
    template_name = "contacts/success.html"



