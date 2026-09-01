import flet as ft


class Campo_tarefa(ft.Row):
    def __init__(self, texto_tarefa):
        super().__init__()

        self.caixa_tarefa_fazer = ft.TextField(value=texto_tarefa)
    
        self.caixa_estado = ft.Text(value="Pendente")
        
        def mudar_texto():
            if self.caixa_estado.value == "Pendente":
                self.caixa_estado.value = "Concluído"
            elif self.caixa_estado.value == "Concluído":
                self.caixa_estado.value = "Pendente"
        
        self.caixa_verificacao = ft.Checkbox(value=0,
                                             on_change=mudar_texto)

        self.caixa_excluir = ft.FloatingActionButton(icon=ft.Icons.DELETE)

        self.caixa_editar = ft.FloatingActionButton(icon=ft.Icons.EDIT)

        self.coluna_botoes = ft.Column(controls=[self.caixa_excluir,self.caixa_editar])

        self.coluna_tarefas = ft.Column(controls=[self.caixa_estado,self.caixa_tarefa_fazer])

        self.controls = [self.caixa_verificacao,self.coluna_tarefas,self.coluna_botoes]



        
