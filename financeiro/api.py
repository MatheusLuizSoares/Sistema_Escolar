# app/financeiro/api.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from matriculas.models import Matricula
from django.db.models import Sum, Q

@api_view(['GET'])
def financeiro_api(request):
    totais = (
        Matricula.objects.values('aluno__id', 'aluno__nome')
        .annotate(
            total_pago=Sum('curso__valor', filter=Q(status='pago')),
            total_devido=Sum('curso__valor', filter=Q(status='pendente'))
        )
    )
    return Response(list(totais))
