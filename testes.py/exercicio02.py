def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

# 6 e 5.9 são casos de limite porque estão muito próximos
# da nota mínima para aprovação.
# A nota 6 é exatamente o limite e o aluno é aprovado.
# Já 5.9 está um pouco abaixo do limite e o aluno é reprovado.
# Teste extra:
# Também considero importante testar uma nota negativa,
# para verificar como a função se comporta nesse caso.
assert situacao_aluno(-1) == "Reprovado"