from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from core.mixins.models import TimestampMixin


class Title(models.TextChoices):
    MR = "Mr", "Mr"
    MRS = "Mrs", "Mrs"
    MISS = "Miss", "Miss"
    MS = "Ms", "Ms"
    DR = "Dr", "Dr"
    PROF = "Prof", "Prof"
    SIR = "Sir", "Sir"


class BookingEnquiry(TimestampMixin):
    """Booking model that represents a user interested in booking a slot"""

    title = models.CharField(max_length=20, choices=Title.choices)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    primary_vehicle_reg = models.CharField(max_length=8, help_text="This would typically be the storage vehicle")
    secondary_vehicle_reg = models.CharField(max_length=8, help_text="This would typically be the towing vehicle")
    address_line_one = models.CharField(max_length=255)
    address_line_two = models.CharField(max_length=255, blank=True)
    postcode = models.CharField(max_length=8)
    contact_number = PhoneNumberField()

    class Meta:
        verbose_name_plural = "Booking Enquiries"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"

