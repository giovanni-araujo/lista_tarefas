import sqlite3
from database.conexao import conectar_bd

def criar_bd():
    #Incluindo na tabela tarefas
    conexao, cursor = conectar_bd()
    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS tarefas(
                        cod_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
                        tarefa TEXT,
                        status TEXT);
                        """)
    
    conexao.commit() #Salvando as alterações
    conexao.close() #Fechando a conexão