from django.db import models

class Pessoa(models.Model):
  nome_completo = models.CharField(max_length=256)
  email_usuario = models.EmailField(max_length=254)
  data_nascimento = models.DateField(null=True)