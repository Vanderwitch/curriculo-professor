from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class AreaPesquisa(models.Model):
    nome = models.CharField(max_length=255)

class Projeto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    ano = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    autores = models.CharField(max_length=255)
    veiculo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

class Orientacao(models.Model):
    nome_orientando = models.CharField(max_length=255)
    nivel = models.CharField(max_length=50)  # ex: Mestrado, Doutorado
    titulo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)


from django.db import models

class AreaPesquisa(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    ano = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    autores = models.TextField()
    veiculo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class Orientacao(models.Model):
    nome_orientando = models.CharField(max_length=255)
    nivel = models.CharField(max_length=50)  # Mestrado, Doutorado, etc.
    titulo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome_orientando} - {self.nivel}"

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.email})"


from django.db import models

class AreaPesquisa(models.Model):
    nome = models.CharField(max_length=255)

class Projeto(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    ano = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

class Publicacao(models.Model):
    titulo = models.CharField(max_length=255)
    autores = models.TextField()
    veiculo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()
    link = models.URLField(blank=True, null=True)

class Orientacao(models.Model):
    nome_orientando = models.CharField(max_length=255)
    nivel = models.CharField(max_length=50)
    titulo = models.CharField(max_length=255)
    ano = models.PositiveIntegerField()

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
