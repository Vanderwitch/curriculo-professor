from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class AreaPesquisaViewSet(viewsets.ModelViewSet):
    queryset = AreaPesquisa.objects.all()
    serializer_class = AreaPesquisaSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer

class OrientacaoViewSet(viewsets.ModelViewSet):
    queryset = Orientacao.objects.all()
    serializer_class = OrientacaoSerializer

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    permission_classes = [IsAuthenticated]
