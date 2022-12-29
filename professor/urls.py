from django.urls import path
from . import views

urlpatterns = [

    path('cadastro/', views.cadastroProfessor, name='professor.cadastro'),
    path('valida_cadastro/',views.validaCadastroProfessor, name='professor.valida'),
    path('listagem/', views.listagemProfessor, name='professor.listagem')
]