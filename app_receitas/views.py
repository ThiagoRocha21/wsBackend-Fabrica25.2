from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReceitaForm
from .models import Receitas, Categoria
import requests
from django.http import JsonResponse



def CadastrarReceitaView(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        else:
            print(form.errors)
    else:
        form = ReceitaForm()
    return render(request, "receitas/paginas/home.html", {"form": form})

def MostrarReceitaView(request):
    obj = Receitas.objects.all()
    return render(request, "receitas/paginas/exibir.html", {"obj": obj})

def AtualizarReceitaView(request, f_id):
    obj = get_object_or_404(Receitas, id=f_id)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
        else:
            print(form.errors)
    else:
        form = ReceitaForm(instance=obj)
    return render(request, "receitas/paginas/home.html", {"form": form})

def deleteReceitaView(request, f_id):
    obj = get_object_or_404(Receitas, id=f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, "receitas/paginas/confirmacao.html", {"obj": obj})


def criar_categorias():
    categorias = ['Sobremesas', 'Massas', 'Saladas']
    for nome in categorias:
        categoria, created = Categoria.objects.get_or_create(nome=nome)
        if created:
            print(f"Categoria '{nome}' criada.")
        else:
            print(f"Categoria '{nome}' já existe.")


def receitas_externas(request):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=pasta"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data) 
    else:
        return JsonResponse({"erro": "API externa indisponível"}, status=500)
    
def mostrar_receitas_api(request):
    return render(request, 'receitas/paginas/api_receitas.html')