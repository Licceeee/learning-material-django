import math
from django.utils.html import format_html


def calc_min_or_hour(minutes):
    """Returns right format of minutes or hours

    Args:

        minutes (float): total minutes

    Returns:

        str: string with minutes or hours and minutes and definition
    """
    if minutes > 60:
        # eg 97.5 - 1.62 - 1.375
        fractional, whole = math.modf(minutes / 60)
        new_frac = fractional * 0.60
        return f"{whole + new_frac:.2f} h"
    return f"{minutes:.2f} m"


def get_video_format(video_url, width, height):
    """returns the image displayed in admin model overview"""
    if video_url:
        return format_html(
            f'<iframe width="{width}" height="{height}" src="{video_url}"'
            f'  title="YouTube video player"'
            f'  frameborder="0" class="video-frame"'
            f'  allow="accelerometer; autoplay; clipboard-write;'
            f'  encrypted-media; gyroscope; picture-in-picture"'
            f'  allowfullscreen>'
            f'</iframe>')
    else:
        return "No Video Found"
