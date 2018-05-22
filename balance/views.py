from django.http import HttpResponse


def index(request):
    return HttpResponse("This is an index of Balance App.")