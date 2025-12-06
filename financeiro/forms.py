from django import forms
from .models import Financeiro

class FinanceiroForm(forms.ModelForm):
    class Meta:
        model = Financeiro
        fields = ['descricao', 'valor', 'data', 'status']
        widgets = {
            'data': forms.DateInput(
                attrs={
                    'type': 'date',        # força HTML5 date input
                    'class': 'form-control' # opcional, para estilizar
                }
            ),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
