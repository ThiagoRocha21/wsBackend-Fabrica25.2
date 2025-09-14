from .models import Receitas
from django import forms 

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
