import mysql.connector

class BancoDado:
    conexao = None

    def __init__(self):
        self.conexao = mysql.connector.connect(user='root', password='1234', database='hamburgueria')

    def busca_dado(self, pesquisa=str(), parametro=()):
        if not isinstance(pesquisa, str) or not isinstance(parametro, tuple):
            return None

        cursor = self.conexao.cursor(buffered=True, dictionary=True)

        cursor.execute(pesquisa, parametro)

        return cursor.fetchall()

    def insere_dado(self, pesquisa=str(), parametro=()):
        if not isinstance(pesquisa, str) or not isinstance(parametro, tuple):
            return None

        cursor = self.conexao.cursor()

        cursor.execute(pesquisa, parametro)

        self.conexao.commit()

        return cursor.lastrowid

    def atualiza_dado(self, pesquisa=str(), parametro=()):
        if not isinstance(pesquisa, str) or not isinstance(parametro, tuple):
            return None

        cursor = self.conexao.cursor()

        cursor.execute(pesquisa, parametro)

        self.conexao.commit()

    def exclui_dado(self, pesquisa=str(), parametro=()):
        if not isinstance(pesquisa, str) or not isinstance(parametro, tuple):
            return None

        cursor = self.conexao.cursor()

        cursor.execute(pesquisa, parametro)

        self.conexao.commit()
