def menu(): 
	while True: 
          print("1. Cadastrar Aluno") 
          print("2. Sair") 
opcao = input("Escolha: ") 
         
if opcao == "1": 
            print("Cadastrando...") 
            
elif opcao == "2": 
            print("Saindo do programa.") 
        	# Por que o programa continua rodando e mostrando o menu mesmo digitando 2? 
            pass 

#CODIGO CORRIGIDO

def menu():
    while True:
        print("\n=== MENU ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("\nCadastrando aluno...")
            # Aqui viria a sua função de cadastro de aluno

        elif opcao == "2":
            print("\nSaindo do programa... Até mais!")
            break  # Interrompe o laço 'while' e encerra o menu

        else:
            print("\nOpção inválida! Por favor, digite 1 ou 2.")


# Executa o menu
menu()