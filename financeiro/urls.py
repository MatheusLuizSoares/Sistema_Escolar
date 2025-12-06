from django.urls import path
from . import views

app_name = 'financeiro'

urlpatterns = [
    path('', views.financeiro_list, name='financeiro_list'),
    path('novo/', views.financeiro_create, name='financeiro_create'),
    path('editar/<int:id>/', views.financeiro_edit, name='financeiro_edit'),
    path('excluir/<int:id>/', views.financeiro_delete, name='financeiro_delete'),
]
