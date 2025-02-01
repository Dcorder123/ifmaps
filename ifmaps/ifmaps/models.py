from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateTimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
