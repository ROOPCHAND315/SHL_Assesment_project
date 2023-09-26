from rest_framework import serializers
from .models import shlModel
class shlSerializer(serializers.ModelSerializer):
    class Meta:
        model=shlModel
        fields='__all__'
