from .models import Property_details
from random import random, randint
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):

	class Meta:
		model = Property_details
		fields = ('property_id','property_title','address','city','state','zip_code','home_type','beds','baths','rooms', 'property_size', 'description', 'other_features')