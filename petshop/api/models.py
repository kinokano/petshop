from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    pass

class Agenda(models.Model):
    nomeCliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    especiePet = models.CharField(max_length=100)
    nomePet = models.CharField(max_length=100)
    portePet = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    statusChoices = [('Pendente ', 'Pendente '), ('Confirmado ', 'Confirmado '), ('Concluído ', 'Concluído '), ('Cancelado ', 'Cancelado ')]
    status = models.CharField(max_length=100, choices=statusChoices, default='Pendente ')
    servicoChoices = [('Veterinario', 'Atendimento Veterinário'),('BanhoTosa', 'Banho & Tosa'),('Adestramento', 'Adestramento'),('Adocao', 'Adoção'),]
    servico = models.CharField(max_length=20, choices=servicoChoices)

    def __str__(self):
        return self.nomeCliente
