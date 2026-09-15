import flet as ft
from component.classe_campo_tarefa import Campo_tarefa
import sqlite3
from database.conexao import conectar_bd
from database.create_database import criar_bd

def main(pagina:ft.Page):
    pagina.window.width = 700
    pagina.window.height = 600
    pagina.title="Lista de Tarefas"
    pagina.horizontal_alignment = "center"
    pagina.bgcolor = "#A6A9FF"
    
    #Criando a tabela de tarefas no banco de dados SQLITE3 
    conexao, cursor = conectar_bd()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tarefas(
                    cod_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
                    tarefa TEXT,
                    status TEXT);
                    """)

    conexao.commit() #Salvando as alterações
    conexao.close() #Fechando a conexão
    

    titulo = ft.Text(value="Lista de Tarefas",
                     size=30)

    lista_campo_tarefas = []

    tarefa = ft.TextField(value="",
                          label="Adicione sua tarefa")

    def excluir_tarefa(campo_tarefa):
        lista_campo_tarefas.remove(campo_tarefa)
    
    def adicionar_tarefa():
        lista_campo_tarefas.append(Campo_tarefa(texto_tarefa=tarefa.value,
                                                funcao_excluir=excluir_tarefa))

        
        

        tarefa.value = ""
  
    botao_adicionar_tarefa = ft.Button(content="Incluir",
                                       on_click=adicionar_tarefa)

    coluna_tarefas = ft.Column(controls=lista_campo_tarefas,
                               )


    linha_tarefa_add = ft.Row(controls=[tarefa,botao_adicionar_tarefa],
                              alignment="center")


        
    pagina.add(titulo)
    pagina.add(linha_tarefa_add)
    pagina.add(coluna_tarefas)

ft.run(main)