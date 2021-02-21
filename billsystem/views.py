from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Commodity, Category
from .serializers import CategorySerializers


# Create your views here.

def index(request):
    return render(request, 'base.html')

def homeView(request):
    commodities = Commodity.objects.all()
    categories = Category.objects.all()
    context = {'commodities':commodities, 'categories':categories}
    return render(request, 'billApp/home.html', context)

def category_products(request, id):
    category = get_object_or_404(Category, id=id)
    serializers = CategorySerializers(category)
    return JsonResponse(serializers.data)