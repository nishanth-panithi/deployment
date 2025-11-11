from rest_framework import serializers
from .models import cloudtable
class cloudtableserializer(serializers.ModelSerializer):
    class Meta:
        model= cloudtable
        fields="__all__"