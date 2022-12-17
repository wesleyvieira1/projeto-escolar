from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=7)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    contato = models.CharField(max_length=11)
    departamento = models.CharField(max_length=50)
    senha = models.CharField(max_length=8)
    confirm_senha = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.nome