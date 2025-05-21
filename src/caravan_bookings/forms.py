from django import forms
from localflavor.gb.forms import GBPostcodeField
from .models import BookingEnquiry


class BookingEnquiryForm(forms.ModelForm):
    postcode = GBPostcodeField()

    class Meta:
        model = BookingEnquiry
        fields = [
            "title",
            "first_name",
            "last_name",
            "primary_vehicle_reg",
            "secondary_vehicle_reg",
            "address_line_one",
            "address_line_two",
            "postcode",
            "contact_number",
        ]
    
    
