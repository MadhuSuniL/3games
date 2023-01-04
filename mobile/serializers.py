from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import HybridImageField

class MobileSerializer(ModelSerializer):
    class Meta:
        model = Mobile_cards
        exclude  = ['charging_speed']
        
        