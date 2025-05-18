from urllib.parse import parse_qsl, urlencode, urlparse

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def generate_canonical_url(context):
    """
    Given a full url. Generate the appropriate canonical url.

    General rule is that everything should point to the core page without any query params.
    Pagination works slightly differently, page 1 should point to the core page, but anything above
    should keep the page in the querystring.
    """
    request = context.get("request")
    if not request:
        return ""

    url = request.build_absolute_uri()
    parts = urlparse(url)
    base_url = request.build_absolute_uri(parts.path)
    querystring_dict = dict(parse_qsl(parts.query))

    # Should only ever contain the page number if it's greater than 1
    page = querystring_dict.get("page")
    if page and int(page) > 1:
        params = {"page": page}
    else:
        params = {}

    querystring = urlencode(params)
    return f"{base_url}?{querystring}" if querystring else base_url


@register.simple_tag(takes_context=True)
def is_noindex(context) -> bool:
    """
    Takes a request and determines whether or not we should add the "noindex" meta tag.
    """
    request = context.get("request")
    if not request:
        return False
    current_page = request.current_page
    # Manually disabled via the page extension. Page extension only exists if it's actually been
    # set manually.
    if hasattr(current_page, "indexextension") and current_page.indexextension.do_not_index:
        return True
    # Search pages should not be indexed
    if request.GET:
        return True
    # By default we should index the page
    return False
