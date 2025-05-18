from django import template
from django.http import QueryDict

register = template.Library()


@register.simple_tag()
def querystring_replace(querystring=None, **params):
    """
    Returns a querystring with certain keys kept and new params added
    """
    result = QueryDict(mutable=True)

    # Add in any existing keys to our new query
    for key in querystring:
        if key not in params:
            result.setlist(key, querystring.getlist(key))

    # Add in our new params
    result.update(**params)

    return "?" + result.urlencode()


@register.simple_tag()
def querystring_remove(querystring, **params):
    """
    Remove a specific key & value pair from a querystring
    """
    result = QueryDict(mutable=True)

    for key in querystring:
        if key in params:
            value_list = querystring.getlist(key)
            try:
                value_list.remove(str(params[key]))
            except ValueError:
                pass

            result.setlist(key, value_list)

    return "?" + result.urlencode()
