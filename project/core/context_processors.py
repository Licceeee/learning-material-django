from isoweek import Week
from datetime import date


def get_global_vars(request):
    """
      The context processor must return a dictionary.
    """
    return {
      'week': Week.thisweek().week,
      'week_year': Week.thisweek().year,
      'today': date.today(),
      }
