from django.db import models
from alunos.models import Aluno
from cursos.models import Curso

class Matricula(models.Model):
    STATUS_CHOICES = (
        ('ativa', 'Ativa'),
        ('cancelada', 'Cancelada'),
        ('concluida', 'Concluída'),
        ('pendente', 'Pendente'),  # útil para financeiro
        ('pago', 'Pago'),           # útil para financeiro
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='matriculas')
    data_matricula = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativa')
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    class Meta:
        unique_together = ('aluno', 'curso')  # evita duplicar matrícula no mesmo curso

    def __str__(self):
        return f"{self.aluno.nome} - {self.curso.nome}"

    @property
    def valor_devido(self):
        """Retorna quanto ainda falta pagar"""
        return max(self.curso.valor_inscricao - self.valor_pago, 0)

    @property
    def is_pago(self):
        """Indica se a matrícula está totalmente paga"""
        return self.valor_devido == 0
