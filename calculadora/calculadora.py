import flet as ft


def main(page:ft.Page):

    #-----------------------------------------------------------VENTANA-----------------------------------------------------------------
    page.title="Calculadora"
    page.window_height=300
    page.window_width=320
   
    


    # ------------------------------------------------------------VARIABLES--------------------------------------------------------------
    resultado=ft.Text(value="0")
    

    #------------------------------------------------------------FUNCIONES--------------------------------------------------------
    def atras(e):
        pass
    def borrar(e):
        resultado.value="0"
        page.update()
    def calculo(e):
        data=e.control.text
        if data =="=":
            try:
                resultado.value=str(eval(resultado.value))
            except Exception as e:
                resultado.value="ERROR"
        else:
            if resultado.value=="0" or resultado.value=="ERROR":
                resultado.value=data
            else:
                resultado.value+=data

        
        page.update()
        


    
    page.add(
            ft.Row(
                controls=[resultado]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="%"),
                    ft.ElevatedButton(text="CE",on_click=borrar),
                    ft.ElevatedButton(text="C",on_click=atras),
                    ft.ElevatedButton(text="*",on_click=calculo)
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="7",on_click=calculo),
                    ft.ElevatedButton(text="8",on_click=calculo),
                    ft.ElevatedButton(text="9",on_click=calculo),
                    ft.ElevatedButton(text="-",on_click=calculo)
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="4",on_click=calculo),
                    ft.ElevatedButton(text="5",on_click=calculo),
                    ft.ElevatedButton(text="6",on_click=calculo),
                    ft.ElevatedButton(text="+",on_click=calculo),
                ]
            ),
            ft.Row(
                [
                    ft.ElevatedButton(text="1",on_click=calculo),
                    ft.ElevatedButton(text="2",on_click=calculo),
                    ft.ElevatedButton(text="3",on_click=calculo),
                    ft.ElevatedButton(text="/",on_click=calculo)
                ]
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="0",on_click=calculo),
                    ft.ElevatedButton(text=",",on_click=calculo),
                    ft.ElevatedButton(text="=",width=130,on_click=calculo,bgcolor="red"),
                ]
            )
        )
   


ft.app(main)
