from aluno import Aluno
from aluno_dao import AlunoDAO


class IntGrafica:   

    def __init__(self) -> None:
        self.adao = AlunoDAO()

    def criar_tabela(self) -> None:
        self.adao.criar_tabela()
        print('Tabela criada com sucesso.')
    
    def inserir(self) -> None:
        print('Cadastrar aluno.')
        matricula = input('Nº de matrícula: ')
        nome = input('Nome: ')
        cpf = input('CPF: ')
        nascimento = input('Data de nascimento (aaaa-mm-aa): ')
        email = input('E-mail: ')

        aluno = Aluno(matricula, cpf, nome, nascimento, email)
        self.adao.inserir(aluno)

    def deletar(self) -> None:
        print('Deletar aluno do sistema.')
        matricula = input('Digite o número de matrícula: ')
        buscar = self.adao.buscar_matricula(matricula)
        if buscar:
            print(buscar)
            controle = input('Deseja deletar o aluno do sistema? [s/n] ')
            controle.lower()
            if controle == 's':
                self.adao.deletar(matricula)
                print('Aluno deletado com sucesso.')
            else:
                print('Aluno não deletado.')
        else:
            print('Aluno não encontrado.')

    def listar_alunos(self) -> None:
        print('Alunos cadastrados no sistema:\n\n')
        print(self.adao.listar_alunos())

    def buscar(self) -> None:
        finalizado = False
        while not finalizado:
            print('1- buscar por número de matrícula.')
            print('2- buscar por CPF.')
            print('3- Sair')

            try:
                opcao = int(input('Digite o número da opção desejada: '))
                if opcao == 1:
                    matricula = input('Número de matrícula: ')
                    buscar = self.adao.buscar_matricula(matricula)
                    if buscar:
                        print(buscar)
                        finalizado = True
                    else:
                        print('Aluno não encontrado.')
                elif opcao == 2:
                    cpf = input('CPF do aluno: ')
                    buscar = self.adao.buscar_cpf(cpf)
                    if buscar:
                        print(buscar)
                        finalizado = True
                    else:
                        print('Aluno não encontrado.')
                elif opcao == 3:
                    finalizado = True
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
            
    def atualizar(self) -> None:
        finalizado = False
        while not finalizado:
            print('|---------<ATUALIZAR>---------|')
            print('|    1- Nome.                 |')
            print('|    2- CPF.                  |')
            print('|    3- Data de nascimento.   |')
            print('|    4- Email.                |')
            print('|    5- Sair.                 |')
            print('|-----------------------------|')
        
            try:
                opcao = int(input('DIgite a opção desejada: '))
                if opcao == 1:
                    matricula = input('Digite o número de matrícula do aluno: ')
                    buscar = self.adao.buscar_matricula(matricula)
                    if buscar:
                        nome = input('Nome: ')
                        self.adao.alterar_nome(matricula, nome)
                        print('Informação alterada com sucesso!')
                    else:
                        print('Aluno não encontrado.')
                elif opcao == 2:
                    matricula = input('Digite o número de matrícula do aluno: ')
                    buscar = self.adao.buscar_matricula(matricula)
                    if buscar:
                        cpf = input('CPF: ')
                        self.adao.alterar_cpf(matricula, cpf)
                        print('Informação alterada com sucesso!')
                    else:
                        print('Aluno não encontrado.')
                elif opcao == 3:
                    matricula = input('Digite o número de matrícula do aluno: ')
                    buscar = self.adao.buscar_matricula(matricula)
                    if buscar:
                        nasc = input('Data de nascimento [aaaa-mm-dd]: ')
                        self.adao.alterar_datanasc(matricula, nasc)
                        print('Informação alterada com sucesso!')
                    else:
                        print('Aluno não encontrado.')
                elif opcao == 4:
                    matricula = input('Digite o número de matrícula do aluno: ')
                    buscar = self.adao.buscar_matricula(matricula)
                    if buscar:
                        email = input('E-mail: ')
                        self.adao.alterar_email(matricula, email)
                        print('Informação alterada com sucesso!')
                    else:
                        print('Aluno não encontrado.')
                elif opcao == 5:
                    finalizado = True
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')
            

    def imprimir_menu(self) -> None:
        print("|------------------<MENU>------------------|")
        print("|       1- Criar tabela                    |")
        print("|       2- Cadastrar aluno                 |")
        print("|       3- Deletar aluno do sistema        |")
        print("|       4- Buscar aluno                    |")
        print("|       5- Atualizar cadastro do aluno     |")
        print("|       6- Listar alunos cadastrados       |")
        print("|       7- Sair                            |")
        print("|------------------------------------------|")

    def main(self) -> None:
        sair = False
        while not sair:
            self.imprimir_menu()
            try:
                opcao = int(input('O que deseja fazer? '))
                if opcao == 1:
                    self.criar_tabela()
                elif opcao == 2:
                    self.inserir()
                elif opcao == 3:
                    self.deletar()
                elif opcao == 4:
                    self.buscar()
                elif opcao == 5:
                    self.atualizar()
                elif opcao == 6:
                    self.listar_alunos()
                elif opcao == 7:
                    sair = True
                else:
                    print('Opção inválida!')
            except ValueError:
                print('Opção inválida. Por favor, digite um número.')


if __name__ == '__main__':
    app = IntGrafica()
    app.main()
