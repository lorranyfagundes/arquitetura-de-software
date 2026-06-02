# interfaces.py
from abc import ABC, abstractmethod

class ICategoriaDAO(ABC):
    @abstractmethod
    def listar_todas(self):
        pass

    @abstractmethod
    def obter_por_id(self, id_categoria):
        pass

    @abstractmethod
    def inserir(self, descricao):
        pass

    @abstractmethod
    def alterar(self, id_categoria, descricao):
        pass

    @abstractmethod
    def excluir(self, id_categoria):
        pass


class IProdutoDAO(ABC):
    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def obter_por_id(self, id_produto):
        pass

    @abstractmethod
    def inserir(self, descricao, preco, estoque, categoria_id):
        pass

    @abstractmethod
    def alterar(self, id_produto, descricao, preco, estoque, categoria_id):
        pass

    @abstractmethod
    def excluir(self, id_produto):
        pass