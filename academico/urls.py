from django.urls import path
from . import views

urlpatterns = [
    path('aluno/cadastro/', views.cadastroAluno, name='aluno.cadastro'),
    path('aluno/valida_cadastro/',views.validaCadastroAluno, name='aluno.valida'),
    path('aluno/listagem/', views.listagemAluno, name='aluno.listagem'),
    path('aluno/visualizar/<int:id>', views.verAluno, name='aluno.vizualizar'),

    path('professor/cadastro/', views.cadastroProfessor, name='professor.cadastro'),
    path('professor/valida_cadastro/',views.validaCadastroProfessor, name='professor.valida'),
    path('professor/listagem/', views.listagemProfessor, name='professor.listagem'),

    path('disciplina/cadastro/', views.cadastroDisciplina, name='disciplina.cadastro'),
    path('disciplina/valida_cadastro/',views.validaCadastroDisciplina, name='disciplina.valida'),

    path('turma/cadastro/', views.cadastroTurma, name='turma.cadastro'),
    path('turma/valida_cadastro/',views.validaCadastroTurma, name='turma.valida')
    
    
]