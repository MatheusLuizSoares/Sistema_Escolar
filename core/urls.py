from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home

from alunos.api import AlunoViewSet
from cursos.api import CursoViewSet
from matriculas.api import MatriculaViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('alunos/', include('alunos.urls')),
    path('cursos/', include('cursos.urls')),
    path('matriculas/', include('matriculas.urls')),
]
