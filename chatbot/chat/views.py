from django.shortcuts import render
from django.http import HttpResponse
from .actions import complete
import requests
# Create your views here.

def hello(request):
    query = request.POST['query']
    if request.method == 'POST' and query:
        url = "https://incoming.xfiv.chat/xtrim/api/v1/buscarEstatusCuenta"
        payload = {"cedula": query}
        response = requests.post(url, json=payload)
        data = response.json()
        contrato = data['dara']['Contrato']['NumeroContrato']
        return render(request, 'base.html', {'response': contrato, 'query': query})
    else:
        return render(request, 'base.html')


def generar_link_de_pago(request):
    cedula = request.POST['cedula']
    email = request.POST['email']