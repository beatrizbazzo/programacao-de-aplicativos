turma = []
opcao = 0

while opcao != 3: #while enquanto
    print("\n--- MENU---") 
    print("1. adicionar aluno")
    print("2. mostrar turma")
    print("3. sair")

    opcao = int(input("escolha uma opção: "))

    if opcao == 1:
        nome = input("digite o nome do aluno: ")
        turma.append(nome) #append Adicionando o nome na lista
        print("aluno adicionado com sucesso!")
        
    elif opcao == 2:
        if len(turma) == 0: #len -> tamanho
            print("A turma está vazia.")
        else:
            for aluno in turma: # for - para - pecorre a minha lista
                print(f"aluno: {aluno}")

    elif opcao == 3:
        print("encerrando o programa...")

    else:
        print("opção invalida, tente novamente. ")


# nomes = ["gabriel","maria","laura"]
# nomes[0]

    