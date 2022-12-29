from django.contrib import admin
from .models import Professor, Aluno, Turma, Disciplina

admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Disciplina)