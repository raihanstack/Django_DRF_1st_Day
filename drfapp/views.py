from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. Django DRF is working!")

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello, API!"})
