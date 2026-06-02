# repositories.py
from .interfaces import ICategoriaDAO, IProdutoDAO

class CategoriaRepository:
    def __init__(self, categoria_dao: ICategoriaDAO):
        # Agora o repositório depende da abstração (interface)
        self.dao = categoria_dao

    def listar_todas(self):
        return self.dao.listar_todas()

    def obter_por_id(self, id_categoria):
        return self.dao.obter_por_id(id_categoria)

    def inserir(self, descricao):
        # Aqui poderiam haver validações de negócio, por exemplo:
        if not descricao:
            raise Exception("Descrição inválida")
        self.dao.inserir(descricao)

    def alterar(self, id_categoria, descricao):
        self.dao.alterar(id_categoria, descricao)

    def excluir(self, id_categoria):
        self.dao.excluir(id_categoria)


class ProdutoRepository:
    def __init__(self, produto_dao: IProdutoDAO):
        self.dao = produto_dao

    def listar_todos(self):
        return self.dao.listar_todos()

    def obter_por_id(self, id_produto):
        return self.dao.obter_por_id(id_produto)

    def inserir(self, descricao, preco, estoque, categoria_id):
        self.dao.inserir(descricao, preco, estoque, categoria_id)

    def alterar(self, id_produto, descricao, preco, estoque, categoria_id):
        self.dao.alterar(id_produto, descricao, preco, estoque, categoria_id)

    def excluir(self, id_produto):
        self.dao.excluir(id_produto)