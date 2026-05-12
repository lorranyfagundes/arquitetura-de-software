from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CategoriaForm, ProdutoForm
from .services import CategoriaService, ProdutoService

cat_service = CategoriaService()
prod_service = ProdutoService()

# CATEGORIAS

def categoria_listar(request):
    """Responsável apenas por exibir a lista de categorias"""
    try:
        registros = cat_service.listar_todas()
        return render(request, 'categorias_listar.html', {'registros': registros})
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})

def categoria_incluir(request):
    """Exibe o formulário vazio para nova categoria"""
    return render(request, 'categorias_editar.html', {
        'acao': 'Inclusão', 
        'form': CategoriaForm()
    })

def categoria_alterar(request, id):
    """Exibe o formulário preenchido para alteração"""
    try:
        registro_dict = cat_service.obter_por_id(id)
        return render(request, 'categorias_editar.html', {
            'acao': 'Alteração', 
            'form': CategoriaForm(initial=registro_dict)
        })
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})

def categoria_excluir(request, id):
    """Exibe o formulário preenchido (em modo leitura) para exclusão"""
    try:
        registro_dict = cat_service.obter_por_id(id)
        return render(request, 'categorias_editar.html', {
            'acao': 'Exclusão', 
            'form': CategoriaForm(initial=registro_dict)
        })
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})

def categoria_salvar(request):
    """Recebe o POST e delega ao serviço a lógica de salvar/excluir"""
    try:
        if request.method == 'POST':
            cat_service.processar_salvar(request.POST)
        return HttpResponseRedirect(reverse("categorias_listar"))
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})


# PRODUTOS

def produto_listar(request):
    """Responsável apenas por exibir a lista de produtos"""
    try:
        registros = prod_service.listar_todos()
        return render(request, 'produtos_listar.html', {'registros': registros})
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})

def produto_incluir(request):
    """Exibe o formulário vazio para novo produto"""
    return render(request, 'produtos_editar.html', {
        'acao': 'Inclusão', 
        'form': ProdutoForm()
    })

def produto_alterar(request, id):
    """Exibe o formulário preenchido para alteração"""
    try:
        registro_dict = prod_service.obter_por_id(id)
        return render(request, 'produtos_editar.html', {
            'acao': 'Alteração', 
            'form': ProdutoForm(initial=registro_dict)
        })
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})

def produto_excluir(request, id):
    """Exibe o formulário preenchido para exclusão"""
    try:
        registro_dict = prod_service.obter_por_id(id)
        return render(request, 'produtos_editar.html', {
            'acao': 'Exclusão', 
            'form': ProdutoForm(initial=registro_dict)
        })
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})

def produto_salvar(request):
    """Recebe o POST e delega ao serviço o processamento"""
    try:
        if request.method == 'POST':
            prod_service.processar_salvar(request.POST)
        return HttpResponseRedirect(reverse("produtos_listar"))
    except Exception as err:
        return render(request, 'home.html', {'ERRO': err})


# OUTROS

def home(request):
    """Exibe a página inicial"""
    return render(request, 'home.html')