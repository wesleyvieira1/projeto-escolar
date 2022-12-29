from django.db import models
from datetime import date

class Professor(models.Model):
    nome_prof = models.CharField(max_length=50)
    cpf_prof = models.CharField(max_length=11)
    rg_prof = models.CharField(max_length=7)
    email_prof = models.EmailField()
    endereco_prof = models.CharField(max_length=50)
    formacao_prof = models.CharField(max_length=50)
    contato_prof = models.CharField(max_length=11)
    turno_prof = models.CharField(max_length=50)
    data_nascimento_prof = models.DateField()
    data_entrada_prof = models.DateField(default=date.today)
    raca_prof = models.CharField(max_length=50)
    sexo_prof = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome_prof
