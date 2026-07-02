import sqlite3


def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("UPDATE alunos SET nome = ?", (novo_nome,))

    conexao.commit()
    conexao.close()


# CODIGO CORRIGIDO

import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE alunos SET nome = ? WHERE id = ?", (novo_nome, id_aluno))

    conexao.commit()
    conexao.close()