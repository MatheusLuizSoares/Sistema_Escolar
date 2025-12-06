from django.shortcuts import render, redirect, get_object_or_404
from .models import Financeiro

from .forms import FinanceiroForm

def financeiro_list(request):
    dados = Financeiro.objects.all()
    return render(request, 'financeiro/list.html', {'dados': dados})


def financeiro_create(request):
    if request.method == 'POST':
        form = FinanceiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('financeiro:financeiro_list')
    else:
        form = FinanceiroForm()
    return render(request, 'financeiro/form.html', {'form': form})


def financeiro_edit(request, id):
    item = get_object_or_404(Financeiro, id=id)
    if request.method == 'POST':
        form = FinanceiroForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('financeiro:financeiro_list')
    else:
        form = FinanceiroForm(instance=item)
    return render(request, 'financeiro/form.html', {'form': form})


def financeiro_delete(request, id):
    item = get_object_or_404(Financeiro, id=id)
    item.delete()
    return redirect('financeiro:financeiro_list')  # <-- CORRIGIDO
