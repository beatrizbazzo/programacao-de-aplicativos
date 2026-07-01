import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas(
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome TEXT NOT NULL
                   
        )           
    ''')
    # o banco nao esta salvando as alteraçoes. por que?
    conexao.close()

    # correçao
      
import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS escolas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    conexao.commit()   # Salva as alterações no banco
    conexao.close()    # Fecha a conexão

# Chama a função
inicializar_banco()
