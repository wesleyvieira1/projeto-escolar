from django.db import models
from aluno.models import Aluno

class Boletim1Bimestre(models.Model):
    nome_aluno_boletim = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota1b1 = models.CharField(max_length=3)
    nota2b1 = models.CharField(max_length=3)
    nota3b1 = models.CharField(max_length=3)
    bimestral1 = models.CharField(max_length=3)
    media1 = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.nome_aluno_boletim
    

class Boletim2Bimestre(models.Model):
    nome_aluno_boletim = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota1b2 = models.CharField(max_length=3)
    nota2b2 = models.CharField(max_length=3)
    nota3b2 = models.CharField(max_length=3)
    bimestral2 = models.CharField(max_length=3)
    media2 = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.nome_aluno_boletim

class Boletim3Bimestre(models.Model):
    nome_aluno_boletim = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota1b3 = models.CharField(max_length=3)
    nota2b3 = models.CharField(max_length=3)
    nota3b3 = models.CharField(max_length=3)
    bimestral3 = models.CharField(max_length=3)
    media3 = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.nome_aluno_boletim

class Boletim4Bimestre(models.Model):
    nome_aluno_boletim = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nota1b4 = models.CharField(max_length=3)
    nota2b4 = models.CharField(max_length=3)
    nota3b4 = models.CharField(max_length=3)
    bimestral4 = models.CharField(max_length=3)
    media4 = models.CharField(max_length=3)

    mediafinal = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.nome_aluno_boletim
