import flet as ft
from classe_campo_tarefa import Campo_tarefa
import sqlite3
from database.conexao import conectar_bd
from database.create_database import criar_bd
from model import model_tarefa

def main(pagina:ft.Page):
    pagina.window.width = 700
    pagina.window.height = 600
    pagina.title="Lista de Tarefas"
    pagina.horizontal_alignment = "center"
    pagina.bgcolor = "#A6A9FF"
    
    criar_bd()
    
    

    titulo = ft.Text(value="Lista de Tarefas",
                     size=30)

    lista_campo_tarefas = []


        

    tarefa = ft.TextField(value="",
                          label="Adicione sua tarefa")

    def excluir_tarefa(campo_tarefa):
        lista_campo_tarefas.remove(campo_tarefa)
        
    #recuperando as tarefas do banco de dados
    tarefas_bd = model_tarefa.recuperar_tarefas()
    for tarefas in tarefas_bd:
        lista_campo_tarefas.append(Campo_tarefa(texto_tarefa=tarefas["tarefa"],
                                          funcao_excluir=excluir_tarefa))
    
    def adicionar_tarefa():
        model_tarefa.inserir_tarefa(tarefa.value)

        lista_campo_tarefas.append(Campo_tarefa(texto_tarefa=tarefa.value,
                                                funcao_excluir=excluir_tarefa))

        
        

        tarefa.value = ""
  
    botao_adicionar_tarefa = ft.Button(content="Incluir",
                                       on_click=adicionar_tarefa,
                                       )

    coluna_tarefas = ft.Column(controls=lista_campo_tarefas,
                               )


    linha_tarefa_add = ft.Row(controls=[tarefa,botao_adicionar_tarefa],
                              alignment="center")


        
    pagina.add(titulo)
    pagina.add(linha_tarefa_add)
    pagina.add(coluna_tarefas)

ft.run(main)