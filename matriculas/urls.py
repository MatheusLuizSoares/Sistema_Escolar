from django.urls import path
from .views import matriculas_list

urlpatterns = [
    path('', matriculas_list),
]
