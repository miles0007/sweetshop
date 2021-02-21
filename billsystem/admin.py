from django.contrib import admin
from .models import Commodity, Category
# Register your models here.

admin.site.register(Category)
admin.site.register(Commodity)