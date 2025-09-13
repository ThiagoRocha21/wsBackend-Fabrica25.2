from .models import Usuario, Receitas, Categorias
from django import forms 

class UsuarioForm:
    class Meta:
        model = Usuario 
        fields = '__all__'

        label = {
            "nome" : "Nome",
            "email" : "E-mail",
            "usuario" : "Usuário",
            "senha" : "Senha",
        }

        widgets = {
            "nome" : forms.TextInput(attrs={"placeholder": "João Maneiro da Silva"}),
            "email" : forms.TextInput(attrs={"placeholder":"joaomaneiro23@gmail.com"}),
            "usuario" : forms.TextInput(attrs={"placeholder": "JoaoManeiro"}),
            "senha" : forms.TextInput(attrs={"placeholder": ""}),
        }

class ReceitaForm:
    class Meta:
        model = Receitas
        fields = '__all__'

        label = {
            "nome_receita" : "Nome da Receita",
            "descricao" : "Descrição",
            "ingredientes" : "Ingredientes",
        }

        widgets = {
            "nome_receita" : forms.TextInput(attrs={"placeholder" : "Pudim de leite"}),
            "descricao" : forms.TextInput(attrs={"placeholder": "Pudim de leite fácil e rápido"}),
            "ingredientes" : forms.TextInput(attrs={"placeholder": "Leite, 2x ovos..."}),
        }