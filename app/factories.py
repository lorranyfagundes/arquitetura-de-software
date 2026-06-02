# factories.py
from .daos import CategoriaDAOSqlite, ProdutoDAOSqlite
from .repositories import CategoriaRepository, ProdutoRepository

class WebStoreFactory:
    @staticmethod
    def obter_categoria_repository() -> CategoriaRepository:
        # Cria o DAO concreto e injeta no Repository
        dao = CategoriaDAOSqlite()
        return CategoriaRepository(dao)

    @staticmethod
    def obter_produto_repository() -> ProdutoRepository:
        dao = ProdutoDAOSqlite()
        return ProdutoRepository(dao)