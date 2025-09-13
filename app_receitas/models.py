from django.db import models

class Categorias(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    usuario = models.CharField(max_length=20)
    senha = models.CharField(max_length=30)
    criado_em = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.nome


class Receitas(models.Model):
    nome_receita = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    ingredientes = models.CharField(max_length=200)

    autor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_receita
# Create your models here.
