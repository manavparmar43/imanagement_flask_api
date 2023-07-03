from app import ma
from marshmallow import Schema, fields, pre_load, post_load,  validates_schema, pre_dump
from .models import *
from Product.serializers import ProductSerializer



class StockSerializer(ma.Schema):
    class Meta:
        fields = ('id','product_key','total_stocks') 
        model = Stock

    product_key = ma.Nested(ProductSerializer(only=("name","category_key",)))
    id = ma.String()
