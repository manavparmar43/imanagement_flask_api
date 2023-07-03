from flask import blueprints, Response, Blueprint, request, jsonify
from User.authentication import token_required
from flask.views import MethodView
from .serializers import * 
from .models import *
from bson.json_util import loads, dumps
from bson import json_util
import json
from flask_restful import Resource, Api


stock_bp = Blueprint('stock', __name__)

api = Api(stock_bp)

class StockApi(Resource):
    method_decorators = [token_required]

    def get(self):
        stock_data = Stock.objects.all()
        stock_serializer = StockSerializer()
        main_data = stock_serializer.dump(stock_data, many=True)
        return jsonify(main_data)

    def post(self):
        return Response("post")    




api.add_resource(StockApi,'/stock')

