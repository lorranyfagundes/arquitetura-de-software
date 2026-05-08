import sys
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
import sqlite3
from .repositories import CategoriaRepository, ProdutoRepository


# formulario utilizado para edicao de registros de categorias
class CategoriaForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)

# Método responsavel por listar, incluir, alterar e excluir as Categorias.

def categorias(request, acao=None, id=None):
    try:
        # Instanciamos o repositório
        repo = CategoriaRepository()

        # 1. Listar registros
        if acao is None:
            registros = repo.listar_todas() # Chamamos o repositório!
            return render(request, 'categorias_listar.html', context={'registros': registros})
        
        # 2. Salvar registro
        elif acao == 'salvar':
            form_data = request.POST
            acao_form = form_data['acao']

            if acao_form == 'Inclusão':
                repo.inserir(form_data['descricao'])
            elif acao_form == 'Exclusão':
                repo.excluir(form_data['id'])
            else:
                repo.alterar(form_data['id'], form_data['descricao'])

            return HttpResponseRedirect(reverse("categorias"))
        
        # 3. Inserir registro (Exibir formulário vazio)
        elif acao == 'incluir':
            return render(request, 'categorias_editar.html',
                           context={'acao': 'Inclusão', 'form': CategoriaForm() })
        
        # 4. Alterar ou excluir registro (Exibir formulário preenchido)
        elif acao in ['alterar', 'excluir']:
            registro_dict = repo.obter_por_id(id) # Chamamos o repositório!
            
            acao_texto = 'Alteração' if acao == 'alterar' else 'Exclusão'
            return render(request, 'categorias_editar.html', 
                           context={'acao': acao_texto, 'form': CategoriaForm(initial=registro_dict) })
        
        else:
            raise Exception('Ação inválida')

    except Exception as err:
        return render(request, 'home.html', context={'ERRO': err})


# formulario utilizado para edicao de registros de produtos
class ProdutoForm(forms.Form):
    id = forms.IntegerField(label='ID', widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)
    descricao = forms.CharField(label='Descrição', max_length=30, required=True)
    preco_unitario = forms.DecimalField(label='Preço Unitário', max_digits=10, decimal_places=2, required=True)
    quantidade_estoque = forms.IntegerField(label='Qtd. Estoque', required=True)
    categoria_id = forms.ChoiceField(label='Categoria', required=True)

    # construtor do Formulario
    def __init__(self, *args, **kwargs):
        # chama construtor da classe-Pai
        super().__init__(*args, **kwargs)
        
        # INSTANCIA O REPOSITÓRIO EM VEZ DE CONECTAR NO BANCO
        repo_categoria = CategoriaRepository()
        
        # Obtém os registros usando o método que já criamos!
        categorias = repo_categoria.listar_todas() 
        
        # carrega as categorias no <select> da página usando o ChoiceField
        self.fields['categoria_id'].choices = categorias

# Método responsavel por listar, incluir, alterar e excluir os Produtos.
def produtos(request, acao=None, id=None):
    try:
        # Instanciamos o repositório de produtos
        repo = ProdutoRepository()

        # 1. Listar registros
        if acao is None:
            registros = repo.listar_todos() # Chamada limpa ao repositório!
            return render(request, 'produtos_listar.html', context={'registros': registros})
        
        # 2. Salvar registro
        elif acao == 'salvar':
            form_data = request.POST
            acao_form = form_data['acao']

            if acao_form == 'Inclusão':
                repo.inserir(
                    form_data['descricao'], 
                    form_data['preco_unitario'], 
                    form_data['quantidade_estoque'], 
                    form_data['categoria_id']
                )
            elif acao_form == 'Exclusão':
                repo.excluir(form_data['id'])
            else:
                repo.alterar(
                    form_data['id'],
                    form_data['descricao'], 
                    form_data['preco_unitario'], 
                    form_data['quantidade_estoque'], 
                    form_data['categoria_id']
                )

            return HttpResponseRedirect(reverse("produtos"))
        
        # 3. Inserir registro
        elif acao == 'incluir':
            return render(request, 'produtos_editar.html',
                           context={'acao': 'Inclusão', 'form': ProdutoForm() })
        
        # 4. Alterar ou excluir registro
        elif acao in ['alterar', 'excluir']:
            # Puxa o dicionário prontinho do banco
            registro_dict = repo.obter_por_id(id)

            acao_texto = 'Alteração' if acao == 'alterar' else 'Exclusão'

            return render(request, 'produtos_editar.html', 
                           context={'acao': acao_texto, 'form': ProdutoForm(initial=registro_dict) })
        
        # 5. Ação INVALIDA
        else:
            raise Exception('Ação inválida')

    except Exception as err:
        return render(request, 'home.html', context={'ERRO': err})

# Exibe a página inicial da aplicação
def home(request):
    '''Exibe a pagina inicial da aplicação'''
    # define a página HTML (template) que deverá será carregada
    template = 'home.html'
    return render(request, template)


