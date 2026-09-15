from database.conexao import conectar_bd


def inserir_tarefa(texto_tarefa):
    conexao, cursor = conectar_bd()
    cursor.execute("""
                                INSERT INTO tarefas (tarefa,status)
                                VALUES (?,?);
                                """,
                                [texto_tarefa, "PENDENTE"])
    conexao.commit()
    conexao.close()


def recuperar_tarefas():
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas