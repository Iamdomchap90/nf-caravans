from django.contrib.admin import options
from django.db import models
from django.utils import timezone

from .widgets import RedactorWidget


class RichTextField(models.TextField):
    """
    Rich text field for use with Redactor
    """

    def formfield(self, **kwargs):
        defaults = {"widget": RedactorWidget}
        defaults.update(kwargs)
        return super().formfield(**defaults)


options.FORMFIELD_FOR_DBFIELD_DEFAULTS[RichTextField] = {"widget": RedactorWidget}


class AutoDateTimeField(models.DateTimeField):
    """
    Field used to set the last updated time automatically
    """

    def pre_save(self, model_instance, add):
        return timezone.now()
