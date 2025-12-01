from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import home
from alunos.views import AlunoViewSet
from cursos.views import CursoViewSet
from matriculas.views import MatriculaViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'matriculas', MatriculaViewSet)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('alunos/', include('alunos.urls')),
    path('cursos/', include('cursos.urls')),
    path('matriculas/', include('matriculas.urls')),
]

    


