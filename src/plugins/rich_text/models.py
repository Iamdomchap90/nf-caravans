from django.utils.html import strip_tags
from django.utils.text import Truncator

from ckeditor.fields import RichTextField
from cms.models import CMSPlugin


class RichText(CMSPlugin):
    """
    Represents rich text block using wysiwyg editor
    """

    content = RichTextField(blank=True)

    def __str__(self):
        return self.excerpt

    @property
    def plain_text(self):
        """
        Returns the rich text without any HTML
        """
        return strip_tags(self.content)

    @property
    def excerpt(self):
        """
        Returns an excerpt of the text in plain text
        """
        return Truncator(self.plain_text).words(num=20)
