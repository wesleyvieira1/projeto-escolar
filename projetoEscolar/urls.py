from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('usuario.urls')),
    path('academico/', include('academico.urls')),
    path('boletim/', include('boletim.urls')),
    #path('turma/', include('turma.urls'))
]
