from django.shortcuts import redirect, render
from .models import Persona

# Create your views here.

def index(request):

    if request.method == 'GET':
        return render(request, 'index.html', {})
    elif request.method == 'POST':

        nombre = request.POST.get('name')
        apellido = request.POST.get('surname')

        print(f'El usuario se llama {nombre} {apellido}')

        return redirect('index')