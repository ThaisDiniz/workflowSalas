from rest_framework import serializers
from .models import Usuario, Sala, Localidade, Reserva


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuario
        fields = '__all__'

class SalaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sala
        fields = '__all__'

class LocalidadeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Localidade
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Reserva
        fields = '__all__'
