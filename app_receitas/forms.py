from .models import Usuario, Receitas, Categorias
from django import forms 

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario 
        fields = '__all__'

        labels = {
            "nome" : "Nome",
            "email" : "E-mail",
            "usuario" : "Usuário",
            "senha" : "Senha",
        }

        widgets = {
            "nome" : forms.TextInput(attrs={"placeholder": "João Maneiro da Silva"}),
            "email" : forms.TextInput(attrs={"placeholder":"joaomaneiro23@gmail.com"}),
            "usuario" : forms.TextInput(attrs={"placeholder": "JoaoManeiro"}),
            "senha" : forms.PasswordInput(attrs={"placeholder": ""}),
        }

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receitas
        fields = '__all__'

        labels = {
            "nome_receita" : "Nome da Receita",
            "descricao" : "Descrição",
            "ingredientes" : "Ingredientes",
        }

        widgets = {
            "nome_receita" : forms.TextInput(attrs={"placeholder" : "Pudim de leite"}),
            "descricao" : forms.TextInput(attrs={"placeholder": "Pudim de leite fácil e rápido"}),
            "ingredientes" : forms.TextInput(attrs={"placeholder": "Leite, 2x ovos..."}),
        }
