from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Task

# Create your views here.

@login_required(login_url='/login/')
def index(request):

    tasks = Task.objects.all()

    return render(request, 'index.html', {'tasks': tasks})

def add(request):

    if request.method == 'POST':
        
        task = request.POST.get('task')

        Task.objects.create(name=task)

        return redirect('index')

def update(request, id):

    task = Task.objects.get(id=id)

    task.done = not task.done

    task.save()

    return redirect('index')

def register(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password)

        return redirect('index')

    else:
        return render(request, 'register.html', {})

def login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            auth_login(request, user)

            return redirect('index')

        else:
            return redirect('login')

    else:
        return render(request, 'login.html', {})

def logout(request):

    auth_logout(request)

    return redirect('login')