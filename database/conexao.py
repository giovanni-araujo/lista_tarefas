import sqlite3

def conectar_bd():
    conexao = sqlite3.connect("bd_tarefas.sqlite")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()
    return conexao, cursor