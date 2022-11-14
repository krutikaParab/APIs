"""Django REST framework takes an existing Django model and converts it to JSON for a REST API. It does this with
model serializers. A model serializer tells Django REST framework how to convert a model instance into JSON and what
data to include. """
from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name", "capital", "area"]

