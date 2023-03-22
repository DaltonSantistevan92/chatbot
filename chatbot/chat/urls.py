from django.urls import path, include
from .views import  hello


app_name = 'chat'

urlpatterns = [
    path('hello/', hello, name='hello'),
]