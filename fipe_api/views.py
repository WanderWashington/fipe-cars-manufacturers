from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from django.db.models import Q

from .models import Marca
from .models import Veiculo
from .models import PaginacaoNumero
from .serializers import MarcaSerializer
from .serializers import VeiculoSerializer


class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    pagination_class = None

    def get_queryset(self):
        q = Q()
        qs = super().get_queryset()

        if 'code' in self.request.GET:
            q &= Q(code=self.request.GET['code'])
        return qs.filter(q)

    
class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    pagination_class = PaginacaoNumero

    def get_queryset(self):
        q = Q()
        qs = super().get_queryset()

        if 'manufacturer' in self.request.GET:
            self.pagination_class = None
            q &= Q(manufacturer=self.request.GET['manufacturer'])
        return qs.filter(q)


