import sqlite3

from filmes import cadastrar_filme, listar_filmes, atualizar_filme, excluir_filme
from atores import cadastrar_atores, listar_atores, atualizar_atores, excluir_atores

def menu():

    while True:

        print("\n===== SISTEMA DE FILMES =====")
        print("1 - Cadastrar filme")
        print("2 - Listar filmes")
        print("3 - Atualizar filme")
        print("4 - Excluir filme")
        print("5 - Cadastrar ator")
        print("6 - Listar atores")
        print("7 - Atualizar ator")
        print("8 - Excluir ator")
        print("9 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_filme()

        elif opcao == "2":
            listar_filmes()

        elif opcao == "3":
            atualizar_filme()

        elif opcao == "4":
            excluir_filme()

        elif opcao == "5":
            cadastrar_atores()

        elif opcao == "6":
            listar_atores()

        elif opcao == "7":
            atualizar_atores()

        elif opcao == "8":
            excluir_atores()

        elif opcao == "9":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


menu()