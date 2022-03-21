class Aluno:
    """
    Essa classe cria um objeto chamado "aluno".

    Args:
        matricula (str): número de matrícula do aluno
        cpf (str): cpf do aluno
        nome (str): nome do aluno
        data_nascimento (str): data de nascimento do aluno 
        email (str): email do aluno
    """

    def __init__(self, matricula: str, cpf: str, nome: str,
                 data_nascimento: str, email: str) -> None:
        """Cria o objeto "aluno".

        Args:
            matricula (str): número de matrícula do aluno
            cpf (str): cpf do aluno
            nome (str): nome do aluno
            data_nascimento (str): data de nascimento do aluno, 'aaaa-mm-dd'
            email (str): email do aluno
        """
        self.matricula = matricula
        self.cpf = cpf
        self.nome = nome
        self.nascimento = data_nascimento
        self.email = email

    def __repr__(self) -> str:
        return '\nNome: ' + self.nome + '\nData de nascimento: ' + \
             self.nascimento + '\nCPF: ' + self.cpf + '\nE-mail: ' + self.email \
             + '\nNº matrícula: ' + self.matricula + '\n' 
