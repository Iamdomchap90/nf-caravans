from django.db import models

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class Form(CMSPlugin):
    """
    Links to a form that is included in the page
    """

    pre_text = models.TextField(blank=True)
    image = FilerImageField(related_name="+", on_delete=models.SET_NULL, null=True, blank=True)
    form = models.ForeignKey(
        to="form_designer.Form", related_name="form_containers", on_delete=models.CASCADE
    )
    post_text = models.TextField(blank=True)
    submit_text = models.CharField(max_length=255, default="Submit")

    def __str__(self):
        return self.form.title
