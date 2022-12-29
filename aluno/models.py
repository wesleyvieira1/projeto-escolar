from django.db import models
from datetime import date

class Aluno(models.Model):
    nome_aluno = models.CharField(max_length=100)
    cpf_aluno = models.CharField(max_length=11)
    rg_aluno = models.CharField(max_length=7)
    email_aluno = models.EmailField()
    endereco_aluno = models.CharField(max_length=50)
    contato_aluno = models.CharField(max_length=11)
    turno_aluno = models.CharField(max_length=50)
    data_nascimento_aluno = models.DateField()
    data_entrada_aluno = models.DateField(default=date.today)
    raca_aluno = models.CharField(max_length=50)
    sexo_aluno = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return str(self.nome_aluno)