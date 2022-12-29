from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.AdicionarNota, name='boletim.cadastro'),
    path('valida_boletim/',views.ValidaBoletim, name='boletim.valida')
    
]