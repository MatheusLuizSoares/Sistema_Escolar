from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Aluno
from .serializers import AlunoSerializer

# API REST
class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
# PÁGINA WEB
def alunos_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/list.html', {'alunos': alunos})
