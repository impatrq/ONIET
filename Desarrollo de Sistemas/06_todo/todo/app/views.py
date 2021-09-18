from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html', {})

def add(request):

    if request.method == 'POST':
        print('Yes')
        print(request.POST)
    else:
        print('No')