# app_cad_usuarios/models.py
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome