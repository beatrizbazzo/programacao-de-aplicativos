import sqlite3

def conectar():
    try:

        conexao = sqlite3.connect("filmes.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao
    except sqlite3.Error as erro:
        print("erro ao conectar com o banco", erro)
        return None
    

def criar_tabelas():
    try:

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


    except sqlite3.Error as erro:
        print("Erro ao criar as tabela:", erro)


def cadastrar_filme():
    try:
        titulo = input("Digite o título do filme: ")
        genero = input("Digite o gênero do filme: ")

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO filmes (titulo, genero) VALUES (?, ?)",
            (titulo, genero)
        )

        conexao.commit()
        conexao.close()

        print("Filme cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar filme:", erro)


def listar_filmes():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM filmes")
        filmes = cursor.fetchall()

        conexao.close()

        if len(filmes) == 0:
            print("Nenhum filme cadastrado.")
        else:
            print("\n--- FILMES ---")
            for filme in filmes:
                print(f"ID: {filme[0]} | Título: {filme[1]} | Gênero: {filme[2]}")

    except sqlite3.Error as erro:
        print("Erro ao listar filmes:", erro)


def atualizar_filme():
    try:
        id_filme = int(input("Digite o ID do filme que deseja atualizar: "))
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
            print("Filme atualizado com sucesso!")
        else:
            print("Filme não encontrado.")

        conexao.close()

    except ValueError:
        print("Digite um ID válido.")

    except sqlite3.Error as erro:
        print("Erro ao atualizar filme:", erro)


def excluir_filme():
    try:
        id_filme = int(input("Digite o ID do filme que deseja excluir: "))

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM filmes WHERE id = ?", (id_filme,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Filme excluído com sucesso!")
        else:
            print("Filme não encontrado.")

        conexao.close()

    except ValueError:
        print("Digite um ID válido.")

    except sqlite3.Error as erro:
        print("Não foi possível excluir o filme:", erro)


def cadastrar_ator():
    try:
        nome = input("Digite o nome do ator: ")
        filme_id = int(input("Digite o ID do filme do ator: "))

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM filmes WHERE id = ?",
            (filme_id,)
        )

        filme = cursor.fetchone()

        if filme is None:
            print("Esse filme não existe.")
            conexao.close()
            return

        cursor.execute(
            "INSERT INTO atores (nome, filme_id) VALUES (?, ?)",
            (nome, filme_id)
        )

        conexao.commit()
        conexao.close()

        print("Ator cadastrado com sucesso!")

    except ValueError:
        print("Digite um ID válido.")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar ator:", erro)


def listar_atores():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT atores.id, atores.nome, atores.filme_id, filmes.titulo
            FROM atores
            INNER JOIN filmes ON atores.filme_id = filmes.id
        """)

        atores = cursor.fetchall()

        conexao.close()

        if len(atores) == 0:
            print("Nenhum ator cadastrado.")
        else:
            print("\n--- ATORES ---")
            for ator in atores:
                print(
                    f"ID: {ator[0]} | Nome: {ator[1]} | "
                    f"ID do filme: {ator[2]} | Filme: {ator[3]}"
                )

    except sqlite3.Error as erro:
        print("Erro ao listar atores:", erro)


def atualizar_ator():
    try:
        id_ator = int(input("Digite o ID do ator que deseja atualizar: "))
        nome = input("Digite o novo nome: ")
        filme_id = int(input("Digite o novo ID do filme: "))

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT id FROM filmes WHERE id = ?",
            (filme_id,)
        )

        filme = cursor.fetchone()

        if filme is None:
            print("Esse filme não existe.")
            conexao.close()
            return

        cursor.execute(
            "UPDATE atores SET nome = ?, filme_id = ? WHERE id = ?",
            (nome, filme_id, id_ator)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Ator atualizado com sucesso!")
        else:
            print("Ator não encontrado.")

        conexao.close()

    except ValueError:
        print("Digite valores válidos.")

    except sqlite3.Error as erro:
        print("Erro ao atualizar ator:", erro)


def excluir_ator():
    try:
        id_ator = int(input("Digite o ID do ator que deseja excluir: "))

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM atores WHERE id = ?",
            (id_ator,)
        )

        conexao.commit()

        if cursor.rowcount > 0:
            print("Ator excluído com sucesso!")
        else:
            print("Ator não encontrado.")

        conexao.close()

    except ValueError:
        print("Digite um ID válido.")

    except sqlite3.Error as erro:
        print("Erro ao excluir ator:", erro)


def menu():
    try:
        criar_tabelas ()

        while True: 
            print("\n===== SISTEMA DE FILMES =====")
            print("1 - cadasrar filme")
            print("2 - listar filme")
            print("3 - atualizar filme ")
            print("4 - excluir filme")
            print("5 - cadastrar ator")
            print("6 - listar ator")
            print("7 - atualizar ator")
            print("8 - excluir ator")
            print("9 - sair")

            opcao = input("escolha uma opcao:")

            if opcao  == "1":
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
                print("programa encerrado.")
                break

            else:
                print("opcao invalida.")


    except Exception as erro:
        print("ocorreu um erro no programa:", erro)



menu()       
