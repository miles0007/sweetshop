from django.urls import path
from .import views

app_name='billing'

urlpatterns = [
    path('', views.homeView, name='home'),
    path('category/<int:id>/', views.category_products, name='category_products')

]