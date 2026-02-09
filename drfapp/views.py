from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. Django DRF is working!")
