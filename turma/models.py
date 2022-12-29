from django.db import models
from disciplina.models import Disciplina

class Turma(models.Model):
    ano_turma = models.CharField(max_length=50, blank=True, null=False)
    horario_inicio_turma = models.CharField(max_length=30)
    horario_fim_turma = models.CharField(max_length=30)
    etapa_turma = models.CharField(max_length=30)
    disciplina_turma = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplinas_turmas')
    dia_turma = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.ano_turma, self.etapa_turma