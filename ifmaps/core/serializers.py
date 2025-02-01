from rest_framework import serializers
from .models import Sala, Evento  # Importando os modelos

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'  # Serializa todos os campos

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
