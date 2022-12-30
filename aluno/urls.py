from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastroAluno, name='aluno.cadastro'),
    path('valida_cadastro/',views.validaCadastroAluno, name='aluno.valida'),
    path('listagem/', views.listagemAluno, name='aluno.listagem'),
    path('visualizar/<int:id>', views.verAluno, name='aluno.vizualizar'),
    path('excluir/<int:pk>', views.deleteAluno.as_view(), name='aluno.delete'),
    path('editar/<int:pk>', views.editarAluno.as_view(), name='aluno.editar')
    ]