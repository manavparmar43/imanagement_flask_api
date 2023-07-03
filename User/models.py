from app import db
from datetime import datetime
from passlib.context import CryptContext
from Product.models import DateTimeMixin


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(DateTimeMixin, db.Document):
    meta = {'collection': 'users'}
    username = db.StringField(default=True)
    email = db.EmailField(unique=True)
    password = db.StringField(default=True)
    active = db.BooleanField(default=False)
    isAdmin = db.BooleanField(default=False)
    timestamp = db.DateTimeField(default=datetime.now())


    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_password(self,password):
        self.password = pwd_context.hash(password)
        super(User, self).save()

    def verify_password(self,password, hashed_password):
        return pwd_context.verify(password, hashed_password)
