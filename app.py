from flask import Flask, Response
from flask_mongoengine import MongoEngine
from mongoengine import *
from flask_restful import Api
import os
import environs

from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mail import Mail, Message

env = environs.Env()
env.read_env()


db = MongoEngine()



# app_env = os.environ["FLASK_ENV"]


flask_app = Flask(__name__)

flask_app.config['MONGODB_SETTINGS'] = {
    'db': 'InventoryManagement',
    'host': 'mongodb+srv://dhruvanshu1775:17753690d@cluster0.u8vtird.mongodb.net/InventoryManagement'
}



   
flask_app.config['MAIL_SERVER']='smtp.gmail.com'
flask_app.config['MAIL_PORT'] = 465
flask_app.config['MAIL_USERNAME'] = 'dhruvanshu.p@latitudetechnolabs.com'
flask_app.config['MAIL_PASSWORD'] = 'Welcome$123'
flask_app.config['MAIL_USE_TLS'] = False
flask_app.config['MAIL_USE_SSL'] = True
mail = Mail(flask_app)


db.init_app(flask_app)

ma = Marshmallow(flask_app)


from Product.controllers import products_bp
from User.controllers import account_bp
from Stocks.controllers import stock_bp
from Ticket.controllers import ticket_blueprint

flask_app.register_blueprint(products_bp)
flask_app.register_blueprint(account_bp)
flask_app.register_blueprint(stock_bp)
flask_app.register_blueprint(ticket_blueprint)


CORS(flask_app)

