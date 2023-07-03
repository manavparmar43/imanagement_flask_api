from flask import blueprints, Response, Blueprint, request, jsonify
from User.authentication import token_required
from flask.views import MethodView
from .serializers import * 
from .models import *
from bson.json_util import loads, dumps
from bson import json_util
import json
from flask_restful import Resource, Api
from Stocks.models import * 
from app import flask_app

ticket_blueprint = Blueprint('ticket',__name__)
api = Api(ticket_blueprint)


class TicketApi(Resource):
    method_decorators = [token_required]

    def get(self):    

        user_data = User.objects.get(id = request.user['user'])

        ticket_data = Ticket.objects.all()


        if user_data.isAdmin is True:
            ticket_serializer = TicketSerializer()
            main_data = ticket_serializer.dump(ticket_data,many=True)
            return jsonify(main_data)

        else:    
            ticket_obj = ticket_data.filter(created_by=user_data)
            ticket_serializer = TicketSerializer()
            main_data = ticket_serializer.dump(ticket_obj,many=True)
            return jsonify(main_data)

    def post(self):
        request_data = request.get_json()
        ticket_data = Ticket(number = 1, description = request_data['description'], problem_type = request_data['request_type'], product_key=request_data['problem_type'], created_by = request.user['user'])
        ticket_data.save()
        return Response("Post Method")    

    def patch(self):
        data = request.get_json()
        ticket_data = Ticket.objects.get(id=data['id'])
        ticket_data.is_solved = True 
        ticket_data.save() 

        stock_data = Stock.objects.get(product_key=ticket_data.product_key.id)
        stock_data.total_stocks =  int(stock_data.total_stocks) - int(1)

    

        stock_data.save()

        return Response("Updated")


@ticket_blueprint.route('/ticketsolve',methods=['GET'])
def Ticketsolveapi():



    ticketsolve=Ticket.objects.filter(is_solved=True).count()
    ticketunsolve=Ticket.objects.filter(is_solved=False).count()
    data = {"solved":ticketsolve,"unsolved":ticketunsolve}
    return jsonify(data)


api.add_resource(TicketApi, '/ticket')

