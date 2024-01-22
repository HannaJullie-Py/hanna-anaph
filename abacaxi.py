import flet as ft

def main(page):

    t= ft.Text()
    usu = ft.TextField(label='Insira seu nome de Usuário', hint_text="Usuário")
    email =  ft.TextField(label='Insira seu Email',hint_text="Email")
    sen = ft.TextField(label='Insira sua Senha',hint_text="Senha" )
    sen1 = ft.TextField(label='Confirme sua Senha',hint_text="Digite Sua Senha Novamente")
    s = ft.ElevatedButton(text= 'Criar', on_click=button_clicked)
    def senha_errada(e):
        if sen1 != sen:
            t.value = 'Senha não confere'
        page.update()
    def button_clicked(e):
        t.value = 'Conta Criada!'
        page.update()
    page.add(t,usu,email,sen,sen1,s)

ft.app(main)