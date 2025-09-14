from django.db import models

class Receitas(models.Model):
    nome_receita = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    ingredientes = models.CharField(max_length=200)
    criado_em = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nome_receita
# Create your models here.
