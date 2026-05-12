from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    # CATEGORIA
    path('categorias/', views.categoria_listar, name='categorias_listar'),
    path('categorias/incluir/', views.categoria_incluir, name='categoria_incluir'),
    path('categorias/alterar/<int:id>/', views.categoria_alterar, name='categoria_alterar'),
    path('categorias/excluir/<int:id>/', views.categoria_excluir, name='categoria_excluir'),
    path('categorias/salvar/', views.categoria_salvar, name='categoria_salvar'),

    # PRODUTO
    path('produtos/', views.produto_listar, name='produtos_listar'),
    path('produtos/incluir/', views.produto_incluir, name='produto_incluir'),
    path('produtos/alterar/<int:id>/', views.produto_alterar, name='produto_alterar'),
    path('produtos/excluir/<int:id>/', views.produto_excluir, name='produto_excluir'),
    path('produtos/salvar/', views.produto_salvar, name='produto_salvar'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)