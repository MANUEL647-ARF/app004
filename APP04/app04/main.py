import flet as ft
from flet_core import elevated_button


def main(page: ft.Page):
    page.title="calculadora"
    page.bgcolor=
    tx1=ft.TextField(label="dame tu primer numero",color="red")
    tx2=ft.TextField(label="dame tu segundo numero",color="red")
    lblresultado=ft.Text("resultado",color="blue")    
    suma=elevated_button
    
    def on_cal_suma(e):
        calc_suma(tx1, tx2, lblresultado)
        page.update()
    
    def on_cal_resta(e):
        calc_resta(tx1, tx2, lblresultado)
        page.update()
    
    def on_cal_multi(e):
        calc_multi(tx1, tx2, lblresultado)
        page.update()
    
    def on_cal_div(e):
        calc_div(tx1, tx2, lblresultado)
        page.update()
    
    def limpiar(e):
        tx1.value=""
        tx2.value=""
        lblresultado.value="resultadio:"
        page.update()
        
    bntsuma=ft.ElevatedButton(text="+",on_click=on_cal_suma)
      bntsuma=ft.ElevatedButton(text="+",on_click=on_cal_suma)
    
    def calc



ft.app(main)
