import sqlite3

opcao = int(input("Digite uma opção (1-3): "))

match opcao:
    case 1:
        print("Cadastrando...")
    case 2:
        print("Listando...")
    case 3:
        print("Saindo...")
    case _:
        print("Opção inválida!")

