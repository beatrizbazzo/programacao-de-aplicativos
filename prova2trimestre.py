import sqlite3

# MEDICO E HOSPITAL

conexao = sqlite3.connect("hospital.db")
conexao.execute("PRAGMA foreign_keys = ON;")
cursor = conexao.cursor()

try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY(id_hospital) REFERENCES hospitais(id)
        )
    ''')

    conexao.commit()
    print("Banco de dados criado com sucesso!")
except sqlite3.Error as erro:
    print("Erro ao criar o banco:", erro)





try:
    nome = input("Nome do hospital: ")
    cidade = input("Cidade: ")

    cursor.execute(
        "INSERT INTO hospitais (nome, cidade) VALUES (?, ?)",
        (nome, cidade)
    )
    conexao.commit()

except sqlite3.Error as erro:
    print("Erro ao cadastrar hospital:", erro)




try:
    nome = input("Nome do médico: ")
    crm = input("CRM: ")
    id_hospital = int(input("ID do hospital: "))

    cursor.execute(
        "INSERT INTO medicos (nome, crm, id_hospital) VALUES (?, ?, ?)",
        (nome, crm, id_hospital)
    )

    conexao.commit()
    print("Médico cadastrado com sucesso!")

except ValueError:
    print("ID inválido.")

except sqlite3.IntegrityError:
    print("Erro: hospital não existe.")

except sqlite3.Error as erro:
    print("Erro:", erro)

conexao.close()




# TRABALHO DE CINEMAS

conexao = sqlite3.connect("cinema.db")
conexao.execute("PRAGMA foreign_keys = ON;")
cursor = conexao.cursor()

try:
    conexao.execute('''
        CREATE TABLE IF NOT EXISTS cinemas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_cinema TEXT NOT NULL,
            shopping TEXT NOT NULL
        )
    ''')

    conexao.execute('''
        CREATE TABLE IF NOT EXISTS salas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_sala INTEGER NOT NULL,
            capacidade INTEGER NOT NULL,
            id_cinema INTEGER NOT NULL,
            FOREIGN KEY (id_cinema) REFERENCES cinemas(id)
            )
    ''')

    conexao.commit()
    print("Banco de dados criado com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao criar o banco:", erro)


try:
    nome_cinema = input("Nome do cinema: ")
    shopping = input("Shopping: ")

    cursor.execute(
        "INSERT INTO cinemas (nome_cinema, shopping) VALUES (?, ?)",
        (nome_cinema, shopping)
    )

    conexao.commit()

except sqlite3.Error as erro:
    print("Erro ao cadastrar cinema:", erro)





try:
    numero_sala = int(input("Número da sala: "))
    capacidade =  int(input("Capacidade: "))
    id_cinema = int(input("ID do cinema: "))

    cursor.execute(
        "INSERT INTO salas (numero_sala, capacidade, id_cinema) VALUES (?, ?, ?)",
        (numero_sala, capacidade, id_cinema)
    )
        
    conexao.commit()
    print("Sala cadastrada com sucesso!")


except ValueError:
    print("Digite apenas números.")

except sqlite3.IntegrityError:
    print("Erro: cinema não existe.")

except sqlite3.Error as erro:
    print("Erro:",  erro)

try:
    cursor.execute("SELECT * FROM salas")
    salas = cursor.fetchall()

    print("\nSalas cadastradas:")
    for sala in salas:
        print(sala)

except sqlite3.Error as erro:
    print("Erro ao listar salas:", erro)

conexao.close()




# TRABALHO DAS ACADEMIAS

conexao = sqlite3.connect("academia.db")
conexao.execute("PRAGMA foreign_keys = ON;")
cursor = conexao.cursor()

try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS academias(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_unidade TEXT NOT NULL,
        bairro TEXT NOT NULL
    )
''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            mensalidade INTEGER NOT NULL,
            id_academia INTEGER NOT NULL,
            FOREIGN KEY (id_academia) REFERENCES academias(id)
    )
''')

    conexao.commit()
    print("Banco de dados criado com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao criar o banco:", erro)



try:
    nome_unidade = input("Nome da unidade: ")
    bairro = input("Bairro: ")

    cursor.execute(
        "INSERT INTO academias (nome_unidade, bairro) VALUES (?, ?)",
        (nome_unidade, bairro)
    )

    conexao.commit()

except sqlite3.Error as erro:
    print("Erro ao cadastrar academia:", erro)



try:
    nome = input("Nome do aluno: ")
    mensalidade = float(input("Mensalidade: "))
    id_academia = int(input("ID academia: "))

    cursor.execute(
        "INSERT INTO alunos (nome, mensalidade, id_academia) VALUES (?, ?, ?)", (nome, mensalidade, id_academia))
    

    conexao.commit()
    print("Aluno cadastrado com sucesso!")

except ValueError:
    print("Digite valores numéricos corretamente.")

except sqlite3.IntegrityError:
    print("Erro: academia não existe.")

except sqlite3.Error as erro:
    print("Erro:", erro)


conexao.close()





# TRABALHO COMPLETO DE DEFESA TECNICA

def inicializar_banco():
    conexao = sqlite3.connect("hotelaria.db")
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS hoteis(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        ''')
    

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quarto(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                numero INTEGER NOT NULL,
                preco_diaria INTEGER NOT NULL,
                id_hotel INTEGER NOT NULL,
                FOREIGN KEY (id_hotel) REFERENCES hoteis(id)
            )
        ''')
    
        conexao.commit()
        print("Banco de dados criado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)

    return conexao

def cadastrar_quarto(conexao):
    try:
        numero = int(input("Número do quarto: "))
        preco = float(input("Preço da diária: "))
        id_hotel = int(input("ID do hotel: "))

        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO quarto (numero, preco_diaria, id_hotel) VALUES (?, ?, ?)", (numero, preco, id_hotel))
    
        conexao.commit()
        print("Quarto cadastrado com sucesso!")

    except ValueError:
        print("Erro: digite números nos campos numéricos.")

    except sqlite3.Error as erro:
        print("Erro no banco:", erro)



conexao = inicializar_banco()


while True:
    print("\n1 - Cadastrar quarto")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_quarto(conexao)
    elif opcao == "0":
        break