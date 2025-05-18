from django import template

register = template.Library()


@register.simple_tag
def thumbnail_bg_position(subject_location, image_width, image_height):
    """
    Given a focal point and the image dimensions, calculate the required
    background position percentage in order to make sure the focal point is
    always in view.
    """
    if not subject_location:
        return "center"

    location_array = subject_location.split(",")
    try:
        x_percentage = (float(location_array[0]) / image_width) * 100
        y_percentage = (float(location_array[1]) / image_height) * 100
        return "{x}% {y}%".format(x=round(x_percentage, 2), y=round(y_percentage, 2))

    except ZeroDivisionError:
        return "center"
