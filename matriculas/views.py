from django.shortcuts import render
from .models import Matricula

def matriculas_list(request):
    matriculas = Matricula.objects.all()
    return render(request, 'matriculas/list.html', {'matriculas': matriculas})
