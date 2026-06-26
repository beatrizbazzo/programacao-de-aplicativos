nota1 = float(input("Digite a sua primeira nota: "))#float numeros nao inteiros ex 4.0
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2  
faltas = int(input("Digite seu número total de faltas: "))#int numeros inteiros ex 40

if faltas > 15:
    print("Reprovado por Faltas.")

elif faltas <= 15:
    if media >= 7:
        print("Aprovado com Sucesso!")
    elif media > 5:
        print("Recuperação.")

    else:
        print("Reprovado por Nota!")  