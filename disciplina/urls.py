from django.urls import path
from . import views

urlpatterns = [

    path('cadastro/', views.cadastroDisciplina, name='disciplina.cadastro'),
    path('valida_cadastro/',views.validaCadastroDisciplina, name='disciplina.valida'),

]