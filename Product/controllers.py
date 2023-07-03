from flask import  Blueprint, Response, jsonify, request
from app import flask_app
from User.authentication import token_required
from Stocks.models import *
from .models import *
from .serializers import *
from flask.views import MethodView, View
import json
from .controllers import *
from Stocks.models import *
from bson.json_util import loads, dumps
from bson import json_util
import random
import string

from flask_restful import Resource, Api

products_bp = Blueprint('product', __name__)

api = Api(products_bp)

class CategoryAPI(Resource):
    method_decorators = [token_required]

    def get(self):
        category_serializer = CategorySerializer(many=True)
        f_data = Category.objects.all()
        data = category_serializer.dump(f_data)
        return jsonify(data)
    
    def post(self):
        name = request.json['name']
        category = Category(name = name)
        category.save()
        return Response(category.name)


class ProductAPI(Resource):
    method_decorators = [token_required]
   

    def get(self):
        product_serializer = ProductSerializer()
        model = Product.objects.all()
        data = product_serializer.dump(model, many=True)
        return  json.loads(json_util.dumps(data))

    def post(self):
        data = request.get_json()
        
        stock = data.get('stock')
        name = data.get('name')
        category = data.get('category')


        main_code_name =  name[0:2]


        N = 5
        product = Product(name=name, category_key=category)
        product.save()


        for i in range(int(stock)):
            res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
            single_product = SingleProduct(product_key=product.id, code=main_code_name+'-'+res )
            single_product.save()

        stock = Stock(product_key=product.id, total_stocks=stock) 
        stock.save()


        return Response("Product Added Succesfully")


class SingleProductApi(Resource):
    method_decorators = [token_required]
    

    def get(self,id):
        product_data = SingleProduct.objects.filter(product_key = id)
        product_serializer = SingleProductSerializer()
        data = product_serializer.dump(product_data, many=True)
        return  json.loads(json_util.dumps(data))

    def post(self,id):
        code = request.json['code']
        product = SingleProduct(product_key=id, code=code)
        product.save()
        try:
            stock_data = Stock.objects.filter(product_key=id)[0]
            main_count = stock_data.total_stocks
            stock_data.total_stocks = main_count + 1
            stock_data.save()
        except:
            stock_data = Stock(product_key = id, total_stocks = 1)
            stock_data.save()

        return Response("Added Successfully")



             
     



## Routers for product model
# products_bp.add_url_rule('/category', view_func=CategoryAPI.as_view('category'))
# products_bp.add_url_rule('/product', view_func=ProductAPI.as_view('product'))
# products_bp.add_url_rule('/bulk_product/<id>', view_func=SingleProductApi.as_view('bulk_product'))

api.add_resource(CategoryAPI, '/categories')
api.add_resource(ProductAPI, '/product')
api.add_resource(SingleProductApi, '/bulk_product/<id>')
