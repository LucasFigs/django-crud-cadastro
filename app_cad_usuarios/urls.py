# app_cad_usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Rota para a página inicial (Criar e Ler)
    path('', views.home, name='home'),
    # Rota para a página de edição (Editar)
    path('edit/<int:id>/', views.edit_usuario, name='edit_usuario'),
    # Rota para a ação de deletar (Excluir)
    path('delete/<int:id>/', views.delete_usuario, name='delete_usuario'),
]