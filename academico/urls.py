from django.urls import path
from . import views

urlpatterns = [

    path('disciplina_cadastro/', views.DisciplinaCreateView.as_view(), name='disciplina.cadastro'),
    #path('valida_cadastro/',views.validaCadastroDisciplina, name='disciplina.valida')

    path('cadastro/', views.cadastroProfessor, name='professor.cadastro'),
    path('valida_cadastro/',views.validaCadastroProfessor, name='professor.valida'),
    path('listagem/', views.listagemProfessor, name='professor.listagem'),
    path('boletim/',views.cadastroBoletim, name='boletim')

]