from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso


# LISTAGEM
def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/list.html', {'cursos': cursos})


# CRIAÇÃO
def curso_create(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        carga_horaria = request.POST.get('carga_horaria')
        ativo = True if request.POST.get('ativo') == "on" else False

        Curso.objects.create(
            nome=nome,
            descricao=descricao,
            carga_horaria=carga_horaria,
            ativo=ativo
        )

        return redirect('cursos_list')

    return render(request, 'cursos/form.html')


# ATUALIZAÇÃO
def curso_update(request, id):
    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        curso.nome = request.POST.get('nome')
        curso.descricao = request.POST.get('descricao')
        curso.carga_horaria = request.POST.get('carga_horaria')
        curso.ativo = True if request.POST.get('ativo') == "on" else False
        curso.save()

        return redirect('cursos_list')

    return render(request, 'cursos/form.html', {'curso': curso})


# EXCLUSÃO
def curso_delete(request, id):
    curso = get_object_or_404(Curso, id=id)
    curso.delete()
    return redirect('cursos_list')
