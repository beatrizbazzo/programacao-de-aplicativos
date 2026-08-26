import sqlite3


def conectar():
    return sqlite3.connect("filmes.db")


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_filme():
    titulo = input("Digite o título do filme: ")
    genero = input("Digite o gênero: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO filmes (titulo, genero) VALUES (?, ?)",
        (titulo, genero)
    )

    conexao.commit()
    conexao.close()

    print("Filme cadastrado!")


def listar_filmes():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM filmes")
    filmes = cursor.fetchall()

    conexao.close()

    print("\n--- FILMES ---")

    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
    else:
        for filme in filmes:
            print(
                "ID:", filme[0],
                "| Título:", filme[1],
                "| Gênero:", filme[2]
            )


def atualizar_filme():
    id_filme = int(input("Digite o ID do filme: "))
    titulo = input("Digite o novo título: ")
    genero = input("Digite o novo gênero: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE filmes SET titulo = ?, genero = ? WHERE id = ?",
        (titulo, genero, id_filme)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Filme atualizado!")
    else:
        print("Filme não encontrado.")

    conexao.close()


def excluir_filme():
    id_filme = int(input("Digite o ID do filme: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM filmes WHERE id = ?",
        (id_filme,)
    )

    conexao.commit()

    if cursor.rowcount > 0:
        print("Filme excluído!")
    else:
        print("Filme não encontrado.")

    conexao.close()