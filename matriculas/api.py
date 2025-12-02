from rest_framework.viewsets import ModelViewSet
from .models import Matricula
from .serializers import MatriculaSerializer

class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
