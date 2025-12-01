from rest_framework.viewsets import ModelViewSet
from .models import Matricula
from .serializers import MatriculaSerializer
from django.shortcuts import render

class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

def matriculas_list(request):
    matriculas = Matricula.objects.all()
    return render(request, 'matriculas/list.html', {'matriculas': matriculas})
