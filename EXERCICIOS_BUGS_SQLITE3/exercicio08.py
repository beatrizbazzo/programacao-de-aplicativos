import sqlite3

def cadastrar_professsor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


    cursor.execute('''
        CREAT TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            cpf TEXT  
        )
    ''')


# CODIGO CORRIGIDO 

import sqlite3

def cadastrar_professsor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


    cursor.execute('''
        CREAT TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
            cpf TEXT UNIQUE 
        )
    ''')