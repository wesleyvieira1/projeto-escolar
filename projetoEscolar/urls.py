from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('usuario.urls')),
    path('aluno/', include('aluno.urls')),
    path('acad/', include('academico.urls')),
    path('turma/', include('turma.urls')),
    path('boletim/', include('boletim.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
