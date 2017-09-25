from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=128)
    data_nascimento = models.DateField(blank=True, null=True)

class Agenda(models.Model):
    nome_agenda = models.CharField(max_length=128)
    usuario = models.ForeignKey(Usuario, null = True, blank=False)
    institucional = models.BooleanField()
    compartilhar = models.BooleanField()
    tipo = models.CharField(max_length=128)

class Compromisso(models.Model):
    nome = models.CharField(max_length=128)
    data = models.DateField(blank=True, null=True)
    agenda = models.ForeignKey(Agenda, null = True, blank=False)
    compartilhar = models.BooleanField()
    usuario = models.ForeignKey(Usuario, null = True, blank=False)

class UsuariosAgenda(models.Model):
    usuario = models.ForeignKey(Usuario, null = True, blank=False)
    agenda = models.ForeignKey(Agenda, null = True, blank=False)
