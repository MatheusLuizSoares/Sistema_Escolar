from django.db import models

class Financeiro(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    status = models.CharField(max_length=20, choices=[('pago', 'Pago'), ('pendente', 'Pendente')])

    def __str__(self):
        return f"{self.descricao} - {self.valor}"
