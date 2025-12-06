from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home

from alunos.api import AlunoViewSet
from cursos.api import CursoViewSet
from matriculas.api import MatriculaViewSet

# Configuração do DRF
router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # Rotas da API
    path('api/', include(router.urls)),

    # URLs de apps (HTML)
    path('alunos/', include('alunos.urls')),
    path('cursos/', include('cursos.urls')),
    path('matriculas/', include('matriculas.urls')),
    path('financeiro/', include('financeiro.urls')),  # <--- importante, já usa app_name
    path('relatorio/', include('relatorio.urls')),
]
