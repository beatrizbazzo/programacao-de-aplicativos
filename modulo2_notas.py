nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2  
faltas = int(input("Digite seu número total de faltas: "))

if faltas > 15:
    print("Reprovado por Faltas.")

if faltas <= 15:
    if media >= 7:
        print("Aprovado com Sucesso!")
    elif media > 5:
        print("Recuperação.")

else:
    print("Reprovado por Nota!") 