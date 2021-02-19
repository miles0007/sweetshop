from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'base.html')

def homeView(request):
    return render(request, 'billApp/home.html')