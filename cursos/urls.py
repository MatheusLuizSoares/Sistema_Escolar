from django.urls import path
from .views import (
    cursos_list,
    curso_create,
    curso_update,
    curso_delete
)

urlpatterns = [
    path('', cursos_list, name='cursos_list'),
    path('novo/', curso_create, name='curso_create'),
    path('editar/<int:id>/', curso_update, name='curso_update'),
    path('excluir/<int:id>/', curso_delete, name='curso_delete'),
]
