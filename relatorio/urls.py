from django.urls import path
from . import views

urlpatterns = [
    path('', views.relatorio_list, name='relatorio_list'),
    path('novo/', views.relatorio_create, name='relatorio_create'),
    path('editar/<int:id>/', views.relatorio_edit, name='relatorio_edit'),
    path('excluir/<int:id>/', views.relatorio_delete, name='relatorio_delete'),
]
