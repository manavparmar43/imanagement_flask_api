from app import db
from datetime import datetime


class DateTimeMixin(db.Document):
    meta ={'allow_inheritance': True, 'abstract': True }

    created_at = db.DateTimeField(nullable=True, default=datetime.now)
    updated_at = db.DateTimeField(nullable=True, on_change=datetime.now)



class Category(DateTimeMixin, db.Document):
    meta = {'collections':'category'}

    name = db.StringField(required=True, max_length=256)

    


class Product(DateTimeMixin, db.Document):
    meta = {'collection': 'products'}

    category_key = db.ReferenceField(Category, nullable=True)
    name         = db.StringField(required=True)


class ProductComponent(DateTimeMixin,db.Document):
    meta = {'collection': 'Product_Componant'}
    product_key = db.ReferenceField(Product, nullable=True)
    name =db.StringField(required=True)

class SingleProduct(DateTimeMixin,db.Document):
    meta = {'collection': 'single product'}

    product_key = db.ReferenceField(Product, nullable=True)
    code        = db.StringField(required=True, nullable=True)
