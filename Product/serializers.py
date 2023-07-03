from app import ma
from .models import *

class CategorySerializer(ma.Schema):
    id = ma.String()    
    class Meta:
        fields = ('id', 'name')


class ProductSerializer(ma.Schema):
    id = ma.String()
    category_key = ma.Nested(CategorySerializer())
    class Meta:
        fields = ('id', 'name', 'category_key')        


class SingleProductSerializer(ma.Schema):
    id = ma.String()
    class Meta:
        fields = ('id', 'product_key.name','code')