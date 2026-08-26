import sqlite3


def conectar():
    return sqlite3.connect("filmes.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS atores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            filme_id INTEGER NOT NULL,
            FOREIGN KEY (filme_id) REFERENCES filmes(id)
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_ator():
    nome = input("Digite o nome do ator: ")
    filme_id = int(input("Digite o ID do filme: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM filmes WHERE id = ?",
        (filme_id,)
    )

    filme = cursor.fetchone()

    if filme is None:
        print("Filme não encontrado.")
    else:
        cursor.execute(
            "INSERT INTO atores (nome, filme_id) VALUES (?, ?)",
            (nome, filme_id)
        )

        conexao.commit()
        print("Ator cadastrado!")

    conexao.close()


def listar_atores():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT atores.id, atores.nome, filmes.titulo
        FROM atores
        INNER JOIN filmes
        ON atores.filme_id = filmes.id
    """)

    atores = cursor.fetchall()

    conexao.close()

    print("\n--- ATORES ---")

    if len(atores) == 0:
        print("Nenhum ator cadastrado.")
    else:
        for ator in atores:
            print(
                "ID:", ator[0],
                "| Nome:", ator[1],
                "| Filme:", ator[2]
            )


def atualizar_ator():
    id_ator = int(input("Digite o ID do ator: "))
    nome = input("Digite o novo nome: ")
    filme_id = int(input("Digite o novo ID do filme: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM filmes WHERE id = ?",
        (filme_id,)
    )

    filme = cursor.fetchone()

    if filme is None:
        print("Filme não encontrado.")
    else:
        cursor.execute(
            "UPDATE atores SET nome = ?, filme_id = ? WHERE id = ?",
            (nome, filme_id, id_ator)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Ator atualizado!")
        else:
            print("Ator não encontrado.")

    conexao.close()


def excluir_ator():
    id_ator = int(input("Digite o ID do ator: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM atores WHERE id = ?",
        (id_ator,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Ator excluído!")
    else:
        print("Ator não encontrado.")

    conexao.close()