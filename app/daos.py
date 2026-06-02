# daos.py
import sqlite3
from .interfaces import ICategoriaDAO, IProdutoDAO

class CategoriaDAOSqlite(ICategoriaDAO):
    def __init__(self):
        self.db_name = 'db_solid.sqlite3'

    def _get_conexao(self):
        conexao = sqlite3.connect(self.db_name)
        conexao.execute("PRAGMA foreign_keys = ON;")
        return conexao

    def listar_todas(self):
        conexao = self._get_conexao()
        sql = 'SELECT id, descricao FROM Categoria ORDER BY descricao'
        registros = conexao.cursor().execute(sql).fetchall()
        conexao.close()
        return registros

    def obter_por_id(self, id_categoria):
        conexao = self._get_conexao()
        sql = f'SELECT id, descricao FROM Categoria WHERE id={id_categoria}'
        registro = conexao.cursor().execute(sql).fetchone()
        conexao.close()
        if registro:
            return {'id': registro[0], 'descricao': registro[1]}
        return None

    def inserir(self, descricao):
        conexao = self._get_conexao()
        sql = f"INSERT INTO Categoria(descricao) VALUES('{descricao}')"
        conexao.cursor().execute(sql)
        conexao.commit()
        conexao.close()

    def alterar(self, id_categoria, descricao):
        conexao = self._get_conexao()
        sql = f"UPDATE Categoria SET descricao = '{descricao}' WHERE id={id_categoria}"
        conexao.cursor().execute(sql)
        conexao.commit()
        conexao.close()

    def excluir(self, id_categoria):
        conexao = self._get_conexao()
        sql = f"DELETE FROM Categoria WHERE id={id_categoria}"
        conexao.cursor().execute(sql)
        conexao.commit()
        conexao.close()


class ProdutoDAOSqlite(IProdutoDAO):
    def __init__(self):
        self.db_name = 'db_solid.sqlite3'

    def _get_conexao(self):
        conexao = sqlite3.connect(self.db_name)
        conexao.execute("PRAGMA foreign_keys = ON;")
        return conexao

    def listar_todos(self):
        conexao = self._get_conexao()
        sql = '''
            SELECT p.id, p.descricao, p.preco_unitario, p.quantidade_estoque, p.categoria_id, c.descricao
            FROM Produto p
            INNER JOIN Categoria c ON p.categoria_id = c.id
            ORDER BY p.descricao
        '''
        registros = conexao.cursor().execute(sql).fetchall()
        conexao.close()
        return registros

    def obter_por_id(self, id_produto):
        conexao = self._get_conexao()
        sql = f'''
            SELECT p.id, p.descricao, p.preco_unitario, p.quantidade_estoque, p.categoria_id, c.descricao
            FROM Produto p
            INNER JOIN Categoria c ON p.categoria_id = c.id
            WHERE p.id = {id_produto}
        '''
        registro = conexao.cursor().execute(sql).fetchone()
        conexao.close()
        if registro:
            return {
                'id': registro[0], 
                'descricao': registro[1],
                'preco_unitario': registro[2],
                'quantidade_estoque': registro[3],
                'categoria_id': registro[4],
                'categoria': registro[5],
            }
        return None

    def inserir(self, descricao, preco, estoque, categoria_id):
        conexao = self._get_conexao()
        sql = f'''
            INSERT INTO Produto (descricao, preco_unitario, quantidade_estoque, categoria_id)
            VALUES ('{descricao}', {preco}, {estoque}, {categoria_id});
        '''
        conexao.cursor().execute(sql)
        conexao.commit()
        conexao.close()

    def alterar(self, id_produto, descricao, preco, estoque, categoria_id):
        conexao = self._get_conexao()
        sql = f'''
            UPDATE Produto 
            SET descricao = '{descricao}', 
                preco_unitario = {preco}, \n                quantidade_estoque = {estoque}, 
                categoria_id = {categoria_id} 
            WHERE id = {id_produto}
        '''
        conexao.cursor().execute(sql)
        conexao.commit()
        conexao.close()

    def excluir(self, id_produto):
        conexao = self._get_conexao()
        sql = f"DELETE FROM Produto WHERE id = {id_produto}"
        conexao.cursor().execute(sql)
        conexao.commit()
        conexao.close()