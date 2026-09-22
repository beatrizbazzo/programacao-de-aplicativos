import sqlite3

from case import cadastrar

print("===== MENU PRINCIPAL =====")
print("1 - Cadastrar")
print("2 - Listar")
print("3 - Atualizar")
print("4 - Excluir")
print("5 - Sair")

opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        cadastrar()

    case 2:
        print("Listando...")

    case 3:
        print("Atualizando...")

    case 4:
        print("Excluindo...")

    case 5:
        print("Saindo do sistema...")

    case _:
        print("Opção inválida!")