from django.urls import path
from . import views

urlpatterns = [
    path('', views.alunos_list, name='alunos_list'),
    path('novo/', views.aluno_create, name='aluno_create'),
    path('editar/<int:id>/', views.aluno_edit, name='aluno_edit'),
    path('excluir/<int:id>/', views.aluno_delete, name='aluno_delete'),
    
]
