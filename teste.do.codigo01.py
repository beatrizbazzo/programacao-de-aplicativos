import sqlite3

opcao = int(input("Digite uma opção (1-3): "))

if opcao == 1:
    print("Cadastrando...")
elif opcao == 2:
    print("Listando...")
elif opcao == 3:
 print("Saindo...")
else:
    print("Opção inválida!")
