import flet as ft
from component.classe_campo_tarefa import Campo_tarefa

def main(pagina:ft.Page):
    pagina.window.width = 700
    pagina.window.height = 600
    pagina.title="Lista de Tarefas"
    pagina.horizontal_alignment = "center"

    titulo = ft.Text(value="Lista de Tarefas",
                     size=30)

    lista_campo_tarefas = []

    tarefa = ft.TextField(value="",
                          label="Adicione sua tarefa")
    
    def adicionar_tarefa():
        lista_campo_tarefas.append(Campo_tarefa(texto_tarefa=tarefa.value))
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