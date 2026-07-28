import sqlite3 
 
def inserir_professor(nome, materia, cpf): 

    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
    	# Existe um erro de digitação no comando SQL (INSERTO).  
    	# Por que o programa mostra "CPF já cadastrado" em vez de avisar sobre o erro de sintaxe? 
        cursor.execute("INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 

    except sqlite3.Error: 
     print("Erro: Este CPF já está cadastrado no sistema!") 

# CODIGO CORRIGIDO

def cadastrar_professor(nome, materia, cpf):
    """Cadastra um novo professor no banco de dados da escola."""
    try:
        # Abrimos a conexão usando o 'with', assim o Python
        # fecha o banco automaticamente, mesmo se der erro!
        with sqlite3.connect("sistema_escola.db") as conexao:
            cursor = conexao.cursor()

            # Comando SQL correto (INSERT INTO)
            sql = """
                INSERT INTO professores (nome, materia, cpf) 
                VALUES (?, ?, ?)
            """

            cursor.execute(sql, (nome, materia, cpf))
            conexao.commit()

        print(f"Professor(a) {nome} cadastrado(a) com sucesso!")

    # Tratando cada tipo de problema de forma individual
    except sqlite3.IntegrityError:
        print(f"Ops! O CPF '{cpf}' já está cadastrado para outro professor.")

    except sqlite3.OperationalError as erro:
        print(
            f"Erro na estrutura do banco ou no comando SQL: {erro}"
        )

    except sqlite3.Error as erro:
        print(f"Aconteceu um erro inesperado com o banco de dados: {erro}")