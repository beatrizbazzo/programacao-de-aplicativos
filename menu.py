import sqlite3

from banco2 import criar_banco
from escolas import cadastrar_escola, listar_escolas
from turma import cadastrar_turma, listar_turmas
from aluno import cadastrar_aluno, listar_alunos


while True:

    print("\n==========================")
    print("      SISTEMA ESCOLAR")
    print("==========================")
    print("1 - Cadastrar escola")
    print("2 - Listar escolas")
    print("3 - Cadastrar turma")
    print("4 - Listar turmas")
    print("5 - Cadastrar aluno")
    print("6 - Listar alunos")
    print("0 - Sair")
    print("==========================")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        cadastrar_escola()

    elif opcao == "2":
        listar_escolas()

    elif opcao == "3":
        cadastrar_turma()

    elif opcao == "4":
        listar_turmas()

    elif opcao == "5":
        cadastrar_aluno()

    elif opcao == "4":
        listar_alunos()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")