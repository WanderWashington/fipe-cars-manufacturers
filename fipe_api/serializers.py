from rest_framework import serializers
# from rest_framework.metadata import BaseMetaData
from .models import Marca
from .models import Veiculo
from datetime import date
from django.conf import settings


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['pk', 'code', 'name']

class VeiculoSerializer(serializers.ModelSerializer):
    # pk_fabricante = serializers.StringRelatedField(source='manufacturer.name')
    # fabricante = MarcaSerializer(many=True, read_only=True, source='marca_set')
    manufacturer_name = serializers.CharField(source='manufacturer.name')
    class Meta:
        model = Veiculo
        fields = ['pk', 'code', 'name', 'manufacturer', 'manufacturer_name']
