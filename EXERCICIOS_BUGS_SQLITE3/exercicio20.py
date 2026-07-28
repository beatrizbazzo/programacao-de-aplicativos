import sqlite3 
 
def cadastrar_escola_manual(): 
	# O aluno resolveu gerar o ID por conta própria 
    id_escola = int(input("Digite o ID para a nova escola: ")) 
    nome = input("Nome da escola: ") 
     
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
	# Se rodar duas vezes com o ID 1, o programa fecha abruptamente (Crash). 
	# Aplique a blindagem protetora necessária: 
    cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
     
    conexao.commit() 
    conexao.close() 

    #CODIGO CORRIGIDO

def cadastrar_escola_manual():
    print("\n--- Cadastrar Escola ---")

    # 1. Trata erro se a pessoa digitar letras no lugar de números
    try:
        id_escola = int(input("Digite o ID para a nova escola: "))
    except ValueError:
        print("Ops! O ID precisa ser um número inteiro.")
        return

    nome = input("Nome da escola: ").strip()

    if not nome:
        print("O nome da escola não pode ficar em branco!")
        return

    # 2. Conexão com o banco usando 'with' para garantir o fechamento automático
    try:
        with sqlite3.connect("sistema_escola.db") as conexao:
            cursor = conexao.cursor()

            # Tenta inserir os dados
            cursor.execute(
                "INSERT INTO escolas (id, nome) VALUES (?, ?)",
                (id_escola, nome),
            )
            conexao.commit()

            print(f"Sucesso! Escola '{nome}' cadastrada com o ID {id_escola}.")

    # 3. Impede o crash se o ID já existir no banco (Chave Primária duplicada)
    except sqlite3.IntegrityError:
        print(
            f"Erro: O ID {id_escola} já está em uso por outra escola no sistema!"
        )

    # 4. Trata outros possíveis erros do banco
    except sqlite3.Error as erro:
        print(f"Erro ao acessar o banco de dados: {erro}")


# Executar a função
cadastrar_escola_manual()


