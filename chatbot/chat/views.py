from django.shortcuts import render
from django.http import HttpResponse
from .actions import complete
import requests
# Create your views here.

def hello(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        response = complete(1, query)
        return render(request, 'base.html', {'response': response})
    else:
        return render(request, 'base.html')


def generar_link_de_pago(request):
    cedula = request.POST['cedula']
    email = request.POST['email']