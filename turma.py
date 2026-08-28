import sqlite3
from banco2 import conectar


def cadastrar_turma():
    nome_turma = input("Digite o nome da turma: ")

    try:
        id_escola = int(input("Digite o ID da escola: "))

        assert nome_turma != "", "O nome da turma não pode ficar vazio!"
        assert id_escola > 0, "O ID da escola deve ser maior que zero!"

        banco = conectar()
        cursor = banco.cursor()

        cursor.execute(
            "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)",
            (nome_turma, id_escola)
        )

        banco.commit()
        banco.close()

        print("Turma cadastrada com sucesso!")

    except ValueError:
        print("Digite um número válido para o ID da escola!")

    except AssertionError as erro:
        print("Erro:", erro)

    except sqlite3.IntegrityError:
        print("Essa escola não existe!")

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)


def listar_turmas():
    try:
        banco = conectar()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM turmas")

        turmas = cursor.fetchall()

        print("\n--- TURMAS ---")

        if len(turmas) == 0:
            print("Nenhuma turma cadastrada.")
        else:
            for turma in turmas:
                print(
                    "ID:", turma[0],
                    "| Nome:", turma[1],
                    "| ID Escola:", turma[2]
                )

        banco.close()

    except sqlite3.Error as erro:
        print("Erro no banco de dados:", erro)