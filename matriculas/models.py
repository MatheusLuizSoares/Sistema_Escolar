from django.db import models
from alunos.models import Aluno
from cursos.models import Curso

class Matricula(models.Model):
    STATUS_CHOICES = (
        ('ativa', 'Ativa'),
        ('trancada', 'Trancada'),
        ('concluida', 'Concluída'),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_matricula = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.aluno} - {self.curso}"
