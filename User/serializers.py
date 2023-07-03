from app import ma
from .models import *

class UserSerializer(ma.Schema):
    class Meta:
        fields = ('id','username','email') 