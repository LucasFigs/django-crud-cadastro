# projeto_cad_usuarios/urls.py
from django.contrib import admin
from django.urls import path, include # Verifique se 'include' está aqui

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_cad_usuarios.urls')), # E esta linha está aqui
]