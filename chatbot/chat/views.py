from django.shortcuts import render
from django.http import HttpResponse
from .actions import complete, code
import requests
# Create your views here.

def hello(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        response = complete(1, query)
        return render(request, 'base.html', {'response': response})
    else:
        return render(request, 'base.html')


def build(request):
    if request.method == 'POST':
        query = request.POST['query']
        response = code(2, query)
        return render(request, 'code.html', {'response': response})
    else:
        return render(request, 'code.html')