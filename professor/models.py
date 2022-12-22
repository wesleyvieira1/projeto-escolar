from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=7)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    formacao = models.CharField(max_length=50)
    contato = models.CharField(max_length=11)
    turno = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    data_entrada = models.DateField()
    raca = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome