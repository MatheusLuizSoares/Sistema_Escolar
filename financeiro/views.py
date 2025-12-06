from django.shortcuts import render, redirect, get_object_or_404
from .models import Financeiro  # ou o nome do seu model financeiro

def financeiro_list(request):
    dados = Financeiro.objects.all()
    return render(request, 'financeiro/list.html', {'dados': dados})

def financeiro_create(request):
    if request.method == 'POST':
        # processar formulário
        ...
        return redirect('financeiro_list')
    return render(request, 'financeiro/form.html')

def financeiro_edit(request, id):
    item = get_object_or_404(Financeiro, id=id)
    if request.method == 'POST':
        # processar edição
        ...
        return redirect('financeiro_list')
    return render(request, 'financeiro/form.html', {'item': item})

def financeiro_delete(request, id):
    item = get_object_or_404(Financeiro, id=id)
    item.delete()
    return redirect('financeiro_list')
