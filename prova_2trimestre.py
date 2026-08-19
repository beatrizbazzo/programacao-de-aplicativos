import sqlite3

def conectar():
    return sqlite3.connect("filmes.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS filmes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            genero TEXT NOT NULL
        )
    """)

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

def cadastrar_ator():
    nome = input("Digite o nome do ator: ")
    filme_id = int(input("Digite o ID do filme: "))

    conexao = conectar()
    cursor = conexao.cursor()

    # Verifica se o filme existe
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

    # Verifica se o filme existe
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

def menu():

    criar_tabelas()

    while True:

        print("\n===== SISTEMA DE FILMES =====")
        print("1 - Cadastrar filme")
        print("2 - Listar filmes")
        print("3 - Atualizar filme")
        print("4 - Excluir filme")
        print("5 - Cadastrar ator")
        print("6 - Listar atores")
        print("7 - Atualizar ator")
        print("8 - Excluir ator")
        print("9 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_filme()

        elif opcao == "2":
            listar_filmes()

        elif opcao == "3":
            atualizar_filme()

        elif opcao == "4":
            excluir_filme()

        elif opcao == "5":
            cadastrar_ator()

        elif opcao == "6":
            listar_atores()

        elif opcao == "7":
            atualizar_ator()

        elif opcao == "8":
            excluir_ator()

        elif opcao == "9":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


menu()