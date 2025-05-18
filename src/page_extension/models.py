from django.db import models

from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from filer.fields.image import FilerImageField


@extension_pool.register
class IndexExtension(PageExtension):
    """
    Allows toggling of page being indexed by search engines
    """

    do_not_index = models.BooleanField(
        default=False,
        help_text="""If ticked, this page will not be indexed by search engines.""",
    )


@extension_pool.register
class SocialShareImageExtension(PageExtension):
    social_share_image = FilerImageField(
        related_name="+",
        help_text="Recommended size: 1500 x 1000 pixels.",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
