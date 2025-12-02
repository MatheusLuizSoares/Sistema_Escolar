from django.shortcuts import render
from .models import Curso

def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/list.html', {'cursos': cursos})
