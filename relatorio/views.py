from django.shortcuts import render, redirect, get_object_or_404
from .models import Relatorio

def relatorio_list(request):
    dados = Relatorio.objects.all()
    return render(request, 'relatorio/list.html', {'dados': dados})

def relatorio_create(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao', '')
        Relatorio.objects.create(titulo=titulo, descricao=descricao)
        return redirect('relatorio_list')
    return render(request, 'relatorio/form.html')

def relatorio_edit(request, id):
    item = get_object_or_404(Relatorio, id=id)
    if request.method == 'POST':
        item.titulo = request.POST.get('titulo')
        item.descricao = request.POST.get('descricao', '')
        item.save()
        return redirect('relatorio_list')
    return render(request, 'relatorio/form.html', {'item': item})

def relatorio_delete(request, id):
    item = get_object_or_404(Relatorio, id=id)
    item.delete()
    return redirect('relatorio_list')
