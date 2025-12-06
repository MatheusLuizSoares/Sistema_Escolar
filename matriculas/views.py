from django.shortcuts import render, redirect, get_object_or_404
from .models import Matricula
from alunos.models import Aluno
from cursos.models import Curso

# LISTAGEM
def matriculas_list(request):
    matriculas = Matricula.objects.all()
    return render(request, 'matriculas/list.html', {'matriculas': matriculas})


# CRIAÇÃO
def matricula_create(request):
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        curso_id = request.POST.get('curso')
        status = request.POST.get('status')

        Matricula.objects.create(
            aluno_id=aluno_id,
            curso_id=curso_id,
            status=status
        )
        return redirect('matriculas_list')

    return render(request, 'matriculas/form.html', {
        'alunos': Aluno.objects.all(),
        'cursos': Curso.objects.all(),
        'status_choices': Matricula.STATUS_CHOICES
    })


# EDIÇÃO
def matricula_update(request, id):
    matricula = get_object_or_404(Matricula, id=id)

    if request.method == 'POST':
        matricula.aluno_id = request.POST.get('aluno')
        matricula.curso_id = request.POST.get('curso')
        matricula.status = request.POST.get('status')
        matricula.save()
        return redirect('matriculas_list')

    return render(request, 'matriculas/form.html', {
        'matricula': matricula,
        'alunos': Aluno.objects.all(),
        'cursos': Curso.objects.all(),
        'status_choices': Matricula.STATUS_CHOICES
    })


# EXCLUSÃO
def matricula_delete(request, id):
    matricula = get_object_or_404(Matricula, id=id)
    matricula.delete()
    return redirect('matriculas_list')
