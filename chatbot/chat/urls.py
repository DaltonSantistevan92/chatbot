from django.urls import path, include
from .views import  hello, build


app_name = 'chat'

urlpatterns = [
    path('xtrim/', hello, name='hello'),
    path('code/', build, name='code'),
]