from rest_framework import serializers
from dishes.models import *


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields='__all__'


        