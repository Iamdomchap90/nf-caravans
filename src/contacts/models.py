from django.db import models

from core.mixins.models import TimestampMixin


class Contact(TimestampMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    enquiry = models.TextField()

    def __str__(self):
        formatted_date = self.created_at.strftime("%d-%m-%Y %H:%M")
        return f"{self.first_name} ({formatted_date})"
