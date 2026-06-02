# services.py
from .factories import WebStoreFactory

class CategoriaService:
    def __init__(self):
        # Agora o Service pede o repositório montado para a Factory
        self.repo = WebStoreFactory.obter_categoria_repository()

    def listar_todas(self):
        return self.repo.listar_todas()

    def obter_por_id(self, id):
        return self.repo.obter_por_id(id)

    def processar_salvar(self, form_data):
        acao = form_data.get('acao')
        id = form_data.get('id')
        descricao = form_data.get('descricao')

        if acao == 'Inclusão':
            self.repo.inserir(descricao)
        elif acao == 'Exclusão':
            self.repo.excluir(id)
        else:
            self.repo.alterar(id, descricao)


class ProdutoService:
    def __init__(self):
        self.repo = WebStoreFactory.obter_produto_repository()

    def listar_todos(self):
        return self.repo.listar_todos()

    def obter_por_id(self, id):
        return self.repo.obter_por_id(id)

    def processar_salvar(self, form_data):
        acao = form_data.get('acao')
        id = form_data.get('id')
        
        if acao == 'Exclusão':
            self.repo.excluir(id)
            return

        dados = {
            'descricao': form_data.get('descricao'),
            'preco': form_data.get('preco_unitario'),
            'estoque': form_data.get('quantidade_estoque'),
            'categoria_id': form_data.get('categoria_id')
        }

        if acao == 'Inclusão':
            self.repo.inserir(dados['descricao'], dados['preco'], dados['estoque'], dados['categoria_id'])
        else:
            self.repo.alterar(id, dados['descricao'], dados['preco'], dados['estoque'], dados['categoria_id'])