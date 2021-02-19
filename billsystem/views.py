from django.shortcuts import render
from .models import Commodity


# Create your views here.

def index(request):
    return render(request, 'base.html')

def homeView(request):
    commodities = Commodity.objects.all()
    context = {'commodities':commodities}
    return render(request, 'billApp/home.html', context)
