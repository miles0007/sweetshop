from .models import Category, Commodity
from rest_framework import routers, serializers




class CommoditySerializers(serializers.ModelSerializer):

    class Meta:
        model = Commodity
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    commodity_set = CommoditySerializers(many=True)
    
    class Meta:
        model = Category
        fields = '__all__'
