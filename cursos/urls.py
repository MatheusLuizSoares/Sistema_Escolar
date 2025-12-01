from django.urls import path
from .views import cursos_list

urlpatterns = [
    path('', cursos_list),
]
