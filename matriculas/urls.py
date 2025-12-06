from django.urls import path
from .views import (
    matriculas_list,
    matricula_create,
    matricula_update,
    matricula_delete
)

urlpatterns = [
    path('', matriculas_list, name='matriculas_list'),
    path('nova/', matricula_create, name='matricula_create'),
    path('editar/<int:id>/', matricula_update, name='matricula_update'),
    path('excluir/<int:id>/', matricula_delete, name='matricula_delete'),
]
