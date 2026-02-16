from rest_framework import serializers
from .models import Table, Category, MenuItem
from decimal import Decimal,ROUND_HALF_UP


class MenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = ('id','name','image','description','price','is_available')


class CategoryWithItemsSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('id','name','description','items')
    
    def get_items(self,obj):
        items = MenuItem.objects.filter(category=obj,is_available=True)
        return MenuItemSerializer(items,many=True).data
    







