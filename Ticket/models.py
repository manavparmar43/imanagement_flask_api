from app import db
from Product.models import *
from User.models import *

class Ticket(DateTimeMixin, db.Document):

    meta = {'collections': 'Ticket'}


    P_choice = (
        ('1', 'Replacement'),
        ('2', 'Requirement'),
    )

    number      = db.IntField()
    description = db.StringField()
    problem_type = db.StringField(max_length=5, choices=P_choice, nullable=True)
    product_key = db.ReferenceField(Product, nullabel=True)
    created_by  = db.ReferenceField(User, nullabel=True)
    problem     = db.StringField()
    is_solved   = db.BooleanField(default=False)
