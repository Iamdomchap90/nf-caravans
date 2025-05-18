from django import template
from django.template.loader import render_to_string

register = template.Library()


def get_pagination_context(obj_list, request):
    querystring = request.GET

    extra_pages_shown = 2
    page_breakpoint = 8
    visible_pages = []
    show_start_dots = False
    show_end_dots = False

    if obj_list.paginator.num_pages > page_breakpoint:
        # Find the index of the current page within all the pages
        pages = list(obj_list.paginator.page_range)
        current_page_index = pages.index(obj_list.number)
        # Take a slice of the list (extra_pages_shown / 2) items either side of the current page
        start_index = int(current_page_index - (extra_pages_shown / 2))
        end_index = int(current_page_index + (extra_pages_shown / 2)) + 1
        visible_pages = pages[
            max(start_index, 1) : min(end_index, obj_list.paginator.num_pages - 1)  # noqa
        ]

        if obj_list.number > (extra_pages_shown + 1):
            show_start_dots = True

        if obj_list.number < (obj_list.paginator.num_pages - extra_pages_shown):
            show_end_dots = True

    return {
        "obj_list": obj_list,
        "querystring": querystring,
        "visible_pages": visible_pages,
        "page_breakpoint": page_breakpoint,
        "show_start_dots": show_start_dots,
        "show_end_dots": show_end_dots,
    }


@register.simple_tag(takes_context=True)
def show_pagination(context, obj_list):
    """
    Template tag to handle the display of paging in the template.
    """
    return render_to_string(
        "pagination/_basic.html",
        get_pagination_context(obj_list, context["request"]),
    )
