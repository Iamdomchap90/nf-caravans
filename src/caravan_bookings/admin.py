from django.contrib import admin

from core.mixins.admin import PUBLISHING_FIELDSET, READONLY_FIELDS, READONLY_FIELDSET

from .models import BookingEnquiry


@admin.register(BookingEnquiry)
class BookingEnquiryAdmin(admin.ModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "contact_number",
        "primary_vehicle_reg",
        "created_at",
        "updated_at",
    ]
    search_fields = ["last_name", "first_name", "primary_vehicle_reg"]
    readonly_fields = READONLY_FIELDS
    fieldsets = [
        ("Personal Details", {"fields": ["title", "first_name", "last_name"]}),
        ("Vehicles", {"fields": ["primary_vehicle_reg", "secondary_vehicle_reg"]}),
        ("Address", {"fields": ["address_line_one", "address_line_two", "postcode"]}),
        (
            "Contact",
            {
                "fields": [
                    "contact_number",
                ]
            },
        ),
        READONLY_FIELDSET,
    ]
