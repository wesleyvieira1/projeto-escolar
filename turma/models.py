from django.db import models
from academico.models import Disciplina
from .choices import *

class Turma(models.Model):           
    ano_turma = models.CharField(max_length=20,choices=choices_ano)
    horario_inicio_turma = models.TimeField()
    horario_fim_turma = models.TimeField()
    etapa_turma = models.CharField(max_length=20,choices=choices_etapa)
    disciplina_turma = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    dia_turma = models.CharField(max_length=20,choices=choices_dia)
    

    def __str__(self) -> str:
        return f'{self.ano_turma} - {self.etapa_turma} | {str(self.disciplina_turma)}'