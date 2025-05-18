from django import template
from django.conf import settings
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def google_tag_manager(javascript=True):
    """
    Renders google tag manager snippets
    """
    template = "js" if javascript else "noscript"

    return render_to_string(
        template_name=f"_components/gtm/{template}.html", context={"gtm_id": settings.GTM_ID}
    )
