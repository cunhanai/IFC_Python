import sqlite3
from dao import DAO
from aluno import Aluno


class AlunoDAO(DAO):

    def __init__(self) -> None:
        self.dao = DAO()

    def criar_tabela(self) -> None:
        """Cria a tabela que armazena os dados dos alunos.

        A tabela tem como parâmetros número de matrícula, CPF, nome, data de
        nascimento e email.
        """
        retorno = self.dao.conectar()
        if retorno:
            self.dao.con.execute("""CREATE TABLE IF NOT EXISTS alunos (
                                matricula text primary key,
                                cpf text not null,
                                nome text not null,
                                data_nascimento date not null,
                                email text not null
                                );""")
            retorno = self.dao.desconectar()
        return retorno

    def inserir(self, aluno: Aluno) -> None:
        """Cadastra um aluno no banco de dados.

        Args:
            aluno (Aluno): dados do aluno no objeto Aluno, dados são inseridos
            por maio da interface.
        """
        self.dao.conectar()
        dados = (aluno.matricula, aluno.cpf, aluno.nome, aluno.nascimento, 
                aluno.email)
        try:
            self.dao.con.execute("""INSERT INTO alunos (
                                        matricula,
                                        cpf,
                                        nome,
                                        data_nascimento,
                                        email)
                                    VALUES (?, ?, ?, ?, ?);""", dados)
        except sqlite3.IntegrityError:
            print('Erro de integridade')
            print(sqlite3.IntegrityError)
        self.dao.con.commit()
        self.dao.desconectar()

    def deletar(self, matricula: str) -> None:
        """Deleta um aluno do sistema a partir do número de matrícula.

        Args:
            matricula (str): Número de matrícula do aluno.
        """
        self.dao.conectar()
        try:
            self.dao.con.execute('DELETE FROM alunos WHERE matricula = ?',
                                 [matricula])
        except sqlite3.IntegrityError:
            print('Erro de integridade.')
            print(sqlite3.IntegrityError)
        self.dao.con.commit()
        self.dao.desconectar()
    
    def listar_alunos(self) -> list:
        """Listar todos os alunos já cadastrados no sistema.

        Returns:
            list: retorna uma lista com todos os alunos.
        """
        self.dao.conectar()
        lista = []
        for linha in self.dao.con.execute('''SELECT * FROM alunos
                                            ORDER BY nome ASC'''):
            aluno = Aluno(linha[0], linha[1], linha[2], linha[3], linha[4])
            lista.append(aluno)
        self.dao.desconectar()
        return lista
        
    def buscar_matricula(self, matricula: str) -> Aluno:
        """Busca um aluno no sistema a partir de seu número de matrícula.

        Args:
            matricula (str): Número de matrícula do aluno

        Returns:
            Aluno: retorna o aluno
        """
        self.dao.conectar()
        aluno = self.dao.con.execute("select * from alunos where matricula == ?",
                                     (matricula, )).fetchone()
        if aluno is not None:
            return Aluno(matricula, aluno[1], aluno[2], aluno[3], aluno[4])
        self.dao.desconectar()

    def buscar_cpf(self, cpf: str) -> Aluno:
        """Busca um aluno no sistema a partir de seu CPF.

        Args:
            cpf (str): CPF do aluno

        Returns:
            Aluno: retorna o aluno
        """
        self.dao.conectar()
        aluno = self.dao.con.execute("select * from alunos where cpf == ?",
                                     (cpf, )).fetchone()
        if aluno is not None:
            return Aluno(aluno[0], cpf, aluno[2], aluno[3], aluno[4])
        self.dao.desconectar()

    def alterar_nome(self, matricula: str, novo_nome: str) -> None:
        """Altera o nome de um aluno no sistema a partir de seu número de matrícula.

        Args:
            matricula (str): Número de matrícula do aluno
            novo_nome (str): Novo nome do aluno
        """
        self.dao.conectar()
        dados = (novo_nome, matricula)
        try:
            self.dao.con.execute('UPDATE alunos SET nome = ?'
                                 'WHERE matricula = ?', dados)
        except sqlite3.IntegrityError:
            print('Erro de integridade.')
            print(sqlite3.IntegrityError)
        self.dao.con.commit()
        self.dao.desconectar()

    def alterar_cpf(self, matricula: str, novo_cpf: str) -> None:
        """Altera o CPF de um aluno no sistema a partir de seu número de matrícula.

        Args:
            matricula (str): Número de matrícula do aluno
            novo_cpf (str): Novo CPF do aluno
        """
        self.dao.conectar()
        dados = (novo_cpf, matricula)
        try:
            self.dao.con.execute('UPDATE alunos SET cpf = ?'
                                 'WHERE matricula = ?', dados)
        except sqlite3.IntegrityError:
            print('Erro de integridade.')
            print(sqlite3.IntegrityError)
        self.dao.con.commit()
        self.dao.desconectar()

    def alterar_datanasc(self, matricula: str, nova_datanasc: str) -> None:
        """Altera a data de nascimento de um aluno no sistema a partir de seu 
            número de matrícula.

        Args:
            matricula (str): Número de matrícula do aluno
            nova_datanasc (str): Nova data de nascumento do aluno
        """
        self.dao.conectar()
        dados = (nova_datanasc, matricula)
        try:
            self.dao.con.execute('UPDATE alunos SET nome = ?'
                                 'WHERE matricula = ?', dados)
        except sqlite3.IntegrityError:
            print('Erro de integridade.')
            print(sqlite3.IntegrityError)
        self.dao.con.commit()
        self.dao.desconectar()
    
    def alterar_email(self, matricula: str, novo_email: str) -> None:
        """Altera o email de um aluno no sistema a partir de seu número de
         matrícula.

        Args:
            matricula (str): Número de matrícula do aluno
            novo_email (str): Novo email do aluno
        """
        self.dao.conectar()
        dados = (novo_email, matricula)
        try:
            self.dao.con.execute('UPDATE alunos SET nome = ?'
                                 'WHERE matricula = ?', dados)
        except sqlite3.IntegrityError:
            print('Erro de integridade.')
            print(sqlite3.IntegrityError)
        self.dao.con.commit()
        self.dao.desconectar()
