from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.boletim, name='boletim.cadastro'),
    path('1bimestre/', views.AdicionarNota1b, name='boletim.1b'),
    path('2bimestre/', views.AdicionarNota2b, name='boletim.2b'),
    path('3bimestre/', views.AdicionarNota3b, name='boletim.3b'),
    path('4bimestre/', views.AdicionarNota4b, name='boletim.4b'),
    path('valida_boletim-1b/',views.ValidaBoletim1, name='boletim.valida-1'),
    path('valida_boletim-2b/',views.ValidaBoletim2, name='boletim.valida-2'),
    path('valida_boletim-3b/',views.ValidaBoletim3, name='boletim.valida-3'),
    path('valida_boletim-4b/',views.ValidaBoletim4, name='boletim.valida-4')
    
]