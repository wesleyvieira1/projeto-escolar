from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.turmaCreateView.as_view(), name='turma.cadastro')
    #path('valida_cadastro/',views.validaCadastroTurma, name='turma.valida')
    ]