import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT,
            id_serie,
            FOREIGN KEY (id_serie) REFERENCES series(id)
        )
    ''')
    conexao.commit()
    conexao.close()


# CODIGO CORRIGIDO

import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT,
            id_serie INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id)
        )
    ''')

    conexao.commit()
    conexao.close()