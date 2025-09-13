from django.shortcuts import render, redirect
from .forms import UsuarioForm, ReceitaForm
from .models import Receitas

# Create your views here.

def CriarUsuarioView(request):
    form = UsuarioForm
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "templates/receitas/paginas/cadastrar.html"
    context = {"form": form}
    return render(request, template_name, context)


def MostrarReceitaView(request):
    obj = Receitas.objects.all()
    template_name = "app_receitas/templates/receitas/paginas/receitas"
    context = {"obj" : obj}
    return render(request, template_name, context)


def AtualizarReceitaView(request, f_id):
    obj = Receitas.objects.get(id = f_id)
    form = ReceitaForm(instance=obj)
    if form.is_valid():
        form.save()
        return redirect("show_url")
    template_name = "app_receitas/templates/receitas/paginas/receitas.html"
    context = {"form": form}
    return render(request, template_name, context)



def deleteReceitaView (request, f_id): 
    obj = Receitas.objects. get (id = f_id) 
    if request.method == "POST" : 
        obj. delete () 
        return redirect ( "show_url" ) 
    template_name = "app_receitas/templates/receitas/paginas/confirmacao.html"
    context = {"obj": obj} 
    return render (request, template_name, context)


def CadastrarReceitaView(request):
    form = ReceitaForm
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "templates/receitas/paginas/receitas.html"





