from django.http import HttpResponse

from .models import Person


def index(request):
    return HttpResponse("<b>Hello</b> <h1>...</h1>")


def detail(request, id):
    return HttpResponse("You're looking at person %s." % id)