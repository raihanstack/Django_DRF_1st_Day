from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello-api/', views.hello_api, name='hello_api'),
]