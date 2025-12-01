from django.urls import path
from .views import alunos_list

urlpatterns = [
    path('', alunos_list),
]
