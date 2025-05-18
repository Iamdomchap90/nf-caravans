from .models import SocialLink


def social_links(request):
    """
    Render the links from the social_links app for use in templates
    """
    return {
        "social_links": SocialLink.objects.filter(is_enabled=True),
    }
