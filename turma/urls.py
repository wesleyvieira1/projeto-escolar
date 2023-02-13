from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.turmaCreateView.as_view(), name='turma.cadastro'),
    path('anexo/',views.cadastroAnexo, name='anexo.cadastro'),
    path('chamada/',views.cadastroChamada,name='chamada.cadastro'),
    path('listagem_turma/',views.Listagem,name='listagem.turma'),
    path('registro_aula/',views.registro,name='registro.turma')

    #path('valida_cadastro/',views.validaCadastroTurma, name='turma.valida')
    ]