from rest_framework.viewsets import ModelViewSet
from .models import Curso
from .serializers import CursoSerializer
from django.shortcuts import render
class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/list.html', {'cursos': cursos})

