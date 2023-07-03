from flask import  Blueprint, Response, jsonify, request, render_template
from flask.views import MethodView
# from app import flask_app

from .models import *
from .authorization import *
from app import mail
from flask_mail import Mail, Message




account_bp = Blueprint('account',__name__,template_folder='templates')




class RegisterApi(MethodView):
    model = User

    def post(self):
        username = request.json['username']
        password = request.json['password']
        email = request.json['email']
        user = self.model.objects.filter(username=username).first()


        if user is not None:
            return Response("User Already Registered")
        else:
           
            user = self.model(username=username, email=email)
            user.get_password(password)
            user.save()    


            token = encode_token(str(user.id))


            msg = Message(
                'Verify Mail',
                sender="dhruvanshu.p@latitudetechnolabs.com",
                recipients = ['dhruvpitroda5@gmail.com']
            )

     

            context = {
                'username': username,
                'token': token,
                'url': request.url_root
            }

            msg.html=render_template('index.html', context=context)
            mail.send(msg)

        return Response("Done",status=201)

class LoginView(MethodView):
    model = User

    def post(self):

        request_data = request.get_json()

        username = request_data['username']
        password = request_data['password']

        user = self.model.objects.filter(username=username).first()
        if user and user.verify_password(password, user.password):

            if user.active is False:
                return Response("Please Verify Account")
            else:
                token = encode_token(str(user.id))

                data = {
                    'token': token,
                    'username': user.username,
                    'admin':user.isAdmin,
                }

                return jsonify(data)
        else:
            return Response("Invalid Credentials", status=401)    


@account_bp.route('/verify-mail', methods=['GET'])
def verify_mail():

    token = request.args.get('token')

    user = decode_token(token)
    
    user = User.objects.get(id=user['user'])
    print(user,'=ssssssss')
    user.active = True 
    user.save()
    return Response("Verified")





account_bp.add_url_rule('/register', view_func=RegisterApi.as_view('register'))
account_bp.add_url_rule('/login', view_func=LoginView.as_view('login'))

