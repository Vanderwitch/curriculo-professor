from rest_framework import serializers
from .models import *

class AreaPesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaPesquisa
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class PublicacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacao
        fields = '__all__'

class OrientacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientacao
        fields = '__all__'

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'
