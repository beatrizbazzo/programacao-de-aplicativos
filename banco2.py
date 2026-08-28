import sqlite3


def conectar():
    banco = sqlite3.connect("gestao_escolar.db")

    banco.execute("PRAGMA foreign_keys = ON")

    return banco

def criar_banco():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()

def criar_tabelas():
    banco = conectar()
    cursor = banco.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT NOT NULL,
            id_escola INTEGER NOT NULL,
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            id_turma INTEGER NOT NULL,
            FOREIGN KEY (id_turma) REFERENCES turmas(id)
        )
    """)

    banco.commit()
    banco.close()

    print("Tabelas criadas com sucesso!")