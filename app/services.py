from .repositories import CategoriaRepository, ProdutoRepository

class CategoriaService:
    def __init__(self):
        self.repo = CategoriaRepository()

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
        self.repo = ProdutoRepository()

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
            self.repo.inserir(**dados)
        else:
            self.repo.alterar(id, **dados)