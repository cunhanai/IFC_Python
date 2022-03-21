import sqlite3

class DAO:
    """Essa classe mãe é responsável por conectar e desconectar do banco de dados.
    """

    def __init__(self) -> None:
        self.con = None

    def conectar(self) -> bool:
        """Conecta com o banco de dados.

        Returns:
            bool: retorna True se concectado com sucesso e False caso não conecte.
        """
        if self.con == None:
            try:
                arq = open('config.txt', 'r')
                nome_arq = arq.readline().replace('\n', '')
                arq.close()
            except Exception:
                nome_arq = 'aluno1.db'
            self.con = sqlite3.connect(nome_arq)
            return True
        return False

    def desconectar(self) -> bool:
        """Desconecta do banco de dados

        Returns:
            bool: Retorna True se desconectado com sucesso e False se não ocorrer.
        """
        if self.con is not None:
            self.con.close()
            self.con = None
            return True
        return False
