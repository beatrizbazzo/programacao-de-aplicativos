import sqlite3 
 
def buscar_dados_dinamicos(nome_tabela, id_registro): 
    conexao = sqlite3.connect('sistema_escola.db')  
    cursor = conexao.cursor() 
     
	# O SQLite joga um erro de sintaxe operacional indicando que não aceita o caractere '?'. 
	# Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança? 
    cursor.execute("SELECT * FROM ? WHERE id = ?", (nome_tabela, id_registro)) 

    print(cursor.fetchone()) 
    conexao.close() 

#CODIGO CORRIGIDO

def buscar_dados_dinamicos(nome_tabela, id_registro):
    """Busca um registro por ID em uma tabela permitida de forma segura."""

    # 1. Lista de tabelas permitidas no sistema (evita SQL Injection)
    TABELAS_PERMITIDAS = {"professores", "alunos", "turmas", "disciplinas"}

    if nome_tabela not in TABELAS_PERMITIDAS:
        print(f"Erro: A tabela '{nome_tabela}' não é válida ou permitida.")
        return None

    try:
        # 2. Uso do 'with' para abrir/fechar a conexão automaticamente
        with sqlite3.connect("sistema_escola.db") as conexao:
            cursor = conexao.cursor()

            # Tabela validada via f-string / ID parametrizado com '?'
            sql = f"SELECT * FROM {nome_tabela} WHERE id = ?"

            cursor.execute(sql, (id_registro,))
            resultado = cursor.fetchone()

            if resultado:
                print(f"Registro encontrado: {resultado}")
            else:
                print(
                    f"Nenhum registro encontrado na tabela '{nome_tabela}' com ID {id_registro}."
                )

            return resultado

    except sqlite3.Error as erro:
        print(f"Erro ao consultar o banco de dados: {erro}")
        return None


# Exemplo de uso:
# buscar_dados_dinamicos("alunos", 1)