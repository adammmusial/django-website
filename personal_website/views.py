from django.http import HtttpResponse


def index(request):
    return HtttpResponse("Homepage")