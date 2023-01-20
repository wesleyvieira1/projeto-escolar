from django.urls import path
from . import views

urlpatterns = [

    path('cadastro/', views.cadastroMensalidade, name='mensalidade.cadastro'),
   

]