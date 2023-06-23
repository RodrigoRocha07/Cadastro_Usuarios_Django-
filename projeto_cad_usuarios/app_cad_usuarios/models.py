from django.db import models

class Usuario(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=245)
    idade = models.IntegerField()