import sqlite3

def cadastrar_lista_alunos():
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)]

    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.executemany(
        "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
        lista
    )

    conexao.commit()
    conexao.close()

#CODIGO CORRIGIDO

def cadastrar_lista_alunos():
    """Cadastra múltiplos alunos de uma só vez no banco de dados."""

    # Lista de tuplas: cada tupla representa um registro (nome, id_turma)
    alunos = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)]

    try:
        # O 'with' abre e fecha a conexão com o banco de forma automática e segura
        with sqlite3.connect("sistema_escola.db") as conexao:
            cursor = conexao.cursor()

            sql = "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)"

            # USANDO EXECUTEMANY: Passamos a instrução SQL e a lista completa
            cursor.executemany(sql, alunos)

            conexao.commit()

        print(f"Sucesso! {len(alunos)} alunos foram cadastrados.")

    except sqlite3.Error as erro:
        print(f"Ops! Ocorreu um erro ao cadastrar a lista de alunos: {erro}")


# Testando a função
cadastrar_lista_alunos()