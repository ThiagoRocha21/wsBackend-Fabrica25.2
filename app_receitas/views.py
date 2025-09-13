from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm, ReceitaForm
from .models import Receitas

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
    return render(request, "receitas/paginas/cadastrar.html", {"obj": obj})

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
