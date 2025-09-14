from django.urls import path
from . import views

urlpatterns = [
    path('', views.CadastrarReceitaView, name='receitas_url'),
    path('show/', views.MostrarReceitaView, name='show_url'),
    path('up/<int:f_id>', views.AtualizarReceitaView, name= 'update_url'),
    path('del/<int:f_id>', views.deleteReceitaView, name= 'delete_url'),
    path('api-receitas/', views.receitas_externas, name='api_receitas'),
    path('receitas-externas/', views.mostrar_receitas_api, name='mostrar_api_receitas'),
]