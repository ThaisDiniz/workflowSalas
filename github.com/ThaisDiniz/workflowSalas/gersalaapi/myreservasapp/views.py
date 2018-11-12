from django.http import JsonResponse
from django_filters import rest_framework as filters
import oauth2_provider.contrib.rest_framework
from rest_condition import Or
from rest_framework import generics , status
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser

from .models import Usuario, Sala, Localidade, Reserva
from .serializers import UsuarioSerializer, SalaSerializer, LocalidadeSerializer, ReservaSerializer


# Create your views here.
# Create your views here.
class UsuarioList(generics.ListCreateAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class SalaList(generics.ListCreateAPIView):

    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class SalaFilter(filters.FilterSet):

    class Meta:

        model = Sala
        fields = '__all__'



class SalaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Sala.objects.all()
    serializer_class = SalaSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = SalaFilter


class LocalidadeList(generics.ListCreateAPIView):

    queryset =  Localidade.objects.all()
    serializer_class = LocalidadeSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class LocalidadeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localidade.objects.all()
    serializer_class = LocalidadeSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'


class ReservaList(generics.ListCreateAPIView):

    queryset =  Reserva.objects.all()
    serializer_class = ReservaSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'

class ReservaFilter(filters.FilterSet):

    data_reserva = filters.DateFilter(name="dataReserva", lookup_expr='dataReserva')

    class Meta:

        model = Reserva
        fields = '__all__'

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    authentication_classes = [oauth2_provider.contrib.rest_framework.OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or( IsAdminUser , oauth2_provider.contrib.rest_framework.TokenHasReadWriteScope )]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ReservaFilter

def token_request(request):
    try:
        new_token = Token.objects.get_or_create(user=request.user)
        return JsonResponse({'token': new_token[0].key}, status=status.HTTP_200_OK)
    except Exception as message:
        return JsonResponse({'messagem': 'voce nao tem permissao.'}, status=status.HTTP_401_UNAUTHORIZED)




