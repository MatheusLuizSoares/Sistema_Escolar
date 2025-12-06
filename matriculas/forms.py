from django import forms
from .models import Matricula

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = '__all__'
        widgets = {
            'aluno': forms.Select(attrs={'class': 'form-select'}),
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            # data_matricula geralmente auto, se exposto use date input:
            # 'data_matricula': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
