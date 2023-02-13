from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/',views.AlunoCreateView.as_view(), name='aluno.cadastro'),
    path('listagem/', views.listagemAluno, name='aluno.listagem'),
    path('visualizar/', views.verAluno.as_view(), name='aluno.vizualizar'),
    path('excluir/<int:pk>', views.deleteAluno.as_view(), name='aluno.delete'),
    path('editar/<int:pk>', views.editarAluno.as_view(), name='aluno.editar')
    ]