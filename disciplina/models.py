from django.db import models
from datetime import date
from professor.models import Professor

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=30, blank=True, null=False)
    professor_disciplina = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome_disciplina