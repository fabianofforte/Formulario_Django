from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial, name='pagina_inicial'),
    path('criar_usuario/', views.criar_usuario, name='criar_usuario'),
    path('atualizar_usuario/<int:usuario_id>/', views.atualizar_usuario, name='atualizar_usuario'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('consultar_usuarios/', views.consultar_usuarios, name='consultar_usuarios'),
]
