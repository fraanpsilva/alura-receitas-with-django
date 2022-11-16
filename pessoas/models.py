from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

# exibindo o nome da pessoa no django-admin
    def __str__(self):
        return self.nome
