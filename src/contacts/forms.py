from django import forms

from .models import Contact


class ContactEnquiryForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "first_name",
            "last_name",
            "email",
            "enquiry",
        ]
