from django.urls import path
from . import views

urlpatterns = [

    path('cadastro/', views.cadastroMensalidade, name='mensalidade.cadastro'),
    path('listagem/', views.listagemMensaliudade, name='mensalidade.listagem')

]