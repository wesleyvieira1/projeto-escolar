from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.turmaCreateView.as_view(), name='turma.cadastro'),
    path('anexo/',views.cadastroAnexo, name='anexo.cadastro'),
    path('chamada/',views.cadastroChamada,name='chamada.cadastro')
    #path('valida_cadastro/',views.validaCadastroTurma, name='turma.valida')
    ]