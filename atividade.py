

def eh_par (numero):
    return numero % 2 == 0

assert eh_par (4) == True

assert eh_par (5) == False

assert eh_par (0) == True

assert eh_par (-3) == False
    

# 02

def situacao_aluno(media):

    if media >= 6:

        return "Aprovado"

    elif media >= 4:

        return "Recuperação"

    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"

assert situacao_aluno (4) != "Aprovado"

assert situacao_aluno(6) == "Aprovado"

assert situacao_aluno(4) == "Recuperação"

assert situacao_aluno(3) == "Reprovado"

assert situacao_aluno(5.9) == "Recuperação"

# 03

def calcular_desconto(preco, percentual):

    return preco - (preco * percentual / 100)

assert calcular_desconto (100, 0 ) == 100

assert calcular_desconto (100, 50) == 50

assert calcular_desconto (100, 10) == 90

assert calcular_desconto (100, 100) == 0

assert calcular_desconto (25.50, 10) == 22.95
 
 # 04 

def pode_entrar(idade, acompanhado):
    if idade >= 18 or acompanhado:
        return True
    return False

assert pode_entrar (20, False) is True

assert pode_entrar (14, False) is True

assert pode_entrar(16, False) is False

assert pode_entrar(18, False) is True

assert pode_entrar(17, True) is True

# 05

def calcular_frete(valor_compra):
    if valor_compra >= 200:
        return 0
    elif valor_compra >= 100:
        return 10
    return 20

assert calcular_frete (50) == 20 

assert calcular_frete (100) == 10

assert calcular_frete (30) == 10

assert calcular_frete (200) == 0

assert calcular_frete (400) == 0

