import sqlite3

def cadastrar_aluno(nome, idade, turma_id):

    assert nome != "", "O nome não pode estar vazio."
    assert idade > 0, "A idade deve ser maior que zero."
    assert turma_id > 0, "O ID da turma deve ser maior que zero."

    try:
        conexao = sqlite3.connect("escola.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO alunos (nome, idade, turma_id)
            VALUES (?, ?, ?)
        """, (nome, idade, turma_id))

        conexao.commit()
        conexao.close()

        print("Aluno cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar aluno:", erro)


def listar_alunos():
    try:
        conexao = sqlite3.connect("escola.db")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT alunos.id, alunos.nome, alunos.idade, turmas.nome
            FROM alunos
            INNER JOIN turmas ON alunos.turma_id = turmas.id
        """)

        alunos = cursor.fetchall()

        conexao.close()

        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n--- Lista de Alunos ---")

            for aluno in alunos:
                print(
                    "ID:", aluno[0],
                    "| Nome:", aluno[1],
                    "| Idade:", aluno[2],
                    "| Turma:", aluno[3]
                )

    except sqlite3.Error as erro:
        print("Erro ao listar alunos:", erro)

    conexao.commit()
    conexao.close()