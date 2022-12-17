from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('usuario.urls')),
    path('aluno/', include('aluno.urls')),
    path('boletim/', include('boletim.urls'))

]
