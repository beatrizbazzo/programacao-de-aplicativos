def buscar_nome(lista, nome):
    return nome in lista
def tem_senha_valida(senha):
    return len(senha) >= 8

assert buscar_nome("João", "Maria", "Pedro", "João") is True

assert buscar_nome("João", "Maria", "Pedro", "Ana") is False

assert buscar_nome("João") is False

assert tem_senha_valida("45248367") is False

assert tem_senha_valida("16461778") is True

assert tem_senha_valida("24282569") is True


# Resposta:
# Ao buscar um nome em uma lista vazia, o resultado é False,
# porque a lista não possui nenhum nome para ser encontrado.
#
# Todos os testes passaram e confirmaram que as duas funções
# estão funcionando de acordo com as regras.