from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

# LIST
def alunos_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/list.html', {'alunos': alunos})

# CRIAR
def aluno_create(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/alunos/')
    return render(request, 'alunos/form.html', {'form': form})

# EDITAR
def aluno_edit(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        form.save()
        return redirect('/alunos/')
    return render(request, 'alunos/form.html', {'form': form})

# EXCLUIR
def aluno_delete(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect('/alunos/')
