from app import ma
from .models import *
from Product.serializers import ProductSerializer

class TicketSerializer(ma.Schema):
    class Meta:
        model = Ticket
        fields = ('id','product_key','created_by.username','description','is_solved', 'problem_type', 'created_at') 
    id = ma.String()
    product_key = ma.Nested(ProductSerializer(only=("name",)))    