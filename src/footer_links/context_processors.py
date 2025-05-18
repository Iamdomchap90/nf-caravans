from .models import FooterLink


def footer_links(request):
    """
    Render the links from the footer_links app for the primary col
    """
    return {"footer_links": FooterLink.objects.filter(is_enabled=True)}
