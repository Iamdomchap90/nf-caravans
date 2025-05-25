from django import forms
from .models import RichText


class RichTextForm(forms.ModelForm):
    class Meta:
        model = RichText
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(attrs={"class": "ckeditor"}),
        }
