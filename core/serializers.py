from rest_framework import serializers
from .models import Dpd, Dpp

class DpdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dpd
        fields = '__all__'

class DppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dpp
        fields = '__all__'
