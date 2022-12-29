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
        return self.nome_aluno

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


class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=30, blank=True, null=False)
    professor_disciplina = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome_disciplina

class Turma(models.Model):
    ano_turma = models.CharField(max_length=50, blank=True, null=False)
    horario_inicio_turma = models.CharField(max_length=30)
    horario_fim_turma = models.CharField(max_length=30)
    etapa_turma = models.CharField(max_length=30)
    disciplina_turma = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='disciplinas_turmas')
    dia_turma = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.ano_turma, self.etapa_turma



