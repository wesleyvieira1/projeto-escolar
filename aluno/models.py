from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=7)
    email = models.EmailField()
    endereco = models.CharField(max_length=50)
    contato = models.CharField(max_length=11)
    turno = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome