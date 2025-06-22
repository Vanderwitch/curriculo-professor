from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Projeto)
admin.site.register(Publicacao)
admin.site.register(Orientacao)
admin.site.register(AreaPesquisa)
admin.site.register(Contato)
