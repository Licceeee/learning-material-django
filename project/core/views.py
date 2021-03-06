from django.views.generic import TemplateView
from django.shortcuts import render


def bad_request(request, exception):
    return render(request, 'core/errors/400.html', status=400)


def permission_denied(request, exception):
    return render(request, 'core/errors/403.html', status=403)


def page_not_found(request, exception):
    return render(request, 'core/errors/404.html', status=404)


def server_error(request):
    return render(request, 'core/errors/500.html', status=500)


def entity_too_large(request):
    return render(request, 'core/errors/413.html', status=413)


class IndexView(TemplateView):
    template_name = 'core/index.html'
