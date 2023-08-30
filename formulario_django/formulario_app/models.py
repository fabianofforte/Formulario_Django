from django.db import models

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    endereco = models.TextField()

    def __str__(self):
        return self.nome_completo

