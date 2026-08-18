import sqlite3

def eh_par (numero):
    return numero % 2 == 0

def eh_impar (numero):
    return numero % 5 == 0

def eh_zero (numero):
    return numero % 0 == 0

def eh_negativo (numero):
    return numero % -3 == 0

# 02

def situacao_aluno(media):

    if media >= 8:

        return "Aprovado"

    elif media >= 5:

        return "Recuperação"

    return "Reprovado"

def situacao_aluno(media):

    if media >= 6:

        return "Aprovado"
    
    elif media >= 3:

        return "Recuperacao"
    
    return "Reprovado"

def situacao_aluno(media):

    if media >= 4:

        return "Aprovado"

    elif media >= 2:

        return "Recuperação"

    return "Reprovado"

def situacao_aluno(media):

    if media >= 3:

        return "Aprovado"

    elif media >= 1:

        return "Recuperação"

    return "Reprovado"

def situacao_aluno(media):

    if media >= 5.9:

        return "Aprovado"

    elif media >= 3:

        return "Recuperação"

    return "Reprovado"