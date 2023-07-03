from app import db 
from Product.models import *



class Stock(DateTimeMixin, db.Document):

    meta = {
        'collections':'stock',
    }

    product_key = db.ReferenceField(Product, nullabel=True)
    total_stocks = db.IntField(nullabel=True, default=0)

