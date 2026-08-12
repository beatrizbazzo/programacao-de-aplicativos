def eh_par(numero):
    return numero % 2 == 0


def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto


def pode_votar(idade):

    if idade < 16:
        return "Não pode votar"
    elif idade < 18 or idade >= 70:
        return "Voto facultativo"
    else:
        return "Voto obrigatório"


assert eh_par(2) is True
assert eh_par(7) is False
assert eh_par(0) is True


assert calcular_desconto(100, 10) == 90
assert calcular_desconto(50, 0) == 50
assert calcular_desconto(200, 100) == 0


assert pode_votar(15) == "Não pode votar"
assert pode_votar(16) == "Voto facultativo"
assert pode_votar(18) == "Voto obrigatório"
assert pode_votar(70) == "Voto facultativo"


print("Todos os testes passaram!")
#PERGUNTAS
# O que acontece quando todos os testes passam?
# O programa continua normalmente e mostra a mensagem “Todos os testes passaram!”.
# Qual teste verifica o valor mínimo para aprovação?
# assert verificar_situacao(6) == "Aprovado"
# Por que testar a nota 5.9 é importante?
# Porque ela está abaixo de 6 e verifica se o programa identifica corretamente uma média que não é suficiente para aprovação.
# Qual teste falha se a aprovação for apenas para média maior que 6?
# Isso acontece porque, usando > 6, uma média exatamente igual a 6 será considerada reprovada.
 
