from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    return JsonResponse({
        'Argentina': 1000412123
    })
    # return render(request, 'index.html', {'nombre': 'Lautaro', 'apellido': 'Paletta', 'numeros': range(0, 20)})