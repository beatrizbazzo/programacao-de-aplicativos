import sqlite3
from banco2 import conectar


def cadastrar_escola():
    nome = input("Digite o nome da escola: ")
    cidade = input("Digite a cidade: ")

    try:
        assert nome != "", "O nome não pode ficar vazio!"
        assert cidade != "", "A cidade não pode ficar vazia!"

        banco = conectar()
        cursor = banco.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )

        banco.commit()
        banco.close()

        print("Escola cadastrada com sucesso!")

    except AssertionError as erro:
        print("Erro:", erro)

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)


def listar_escolas():
    try:
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM escolas")

        escolas = cursor.fetchall()

        print("\n--- ESCOLAS ---")

        for escola in escolas:
            print(
                "ID:", escola[0],
                "| Nome:", escola[1],
                "| Cidade:", escola[2]
            )

        banco.close()

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)