import sqlite3


def criar_bd():
    #Incluindo na tabela tarefas
    conexao, cursor = conectar_bd()
    cursor.execute("""
                            INSERT INTO tarefas (tarefa,status)
                            VALUES (?,?);
                            """,
                            [tarefa.value, "PENDENTE"])
    conexao.commit()
    conexao.close()