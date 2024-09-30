import flet as ft
import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyBhyC5lYSrrw3Z-ffnsO1le_w_sRQyzU_8",
  'authDomain': "login-a23af.firebaseapp.com",
  'projectId': "login-a23af",
  'storageBucket': "login-a23af.appspot.com",
  'databaseURL': 'https://login.firebaseio.com',
  'messagingSenderId': "976239361302",
  'appId': "1:976239361302:web:2ca0667ac4d57c9af3e437",
  'measurementId': "G-EKDKV1Y7YB"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



def main(page: ft.Page):
    page.title = 'Meu APP';
    page.window.width = 400
    page.window.height = 500
    page.theme_mode = 'dark'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 20

    def btn_login(e):
        try:
            auth.sign_in_with_email_and_password(usuario.value, senha.value)
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='Logado com Sucesso'
                ),
                bgcolor='green',
                action='OK',
                duration=3000
            )
            #page.overlay.append(snack_bar)
            #snack_bar.open()
            page.snack_bar.open = True

            usuario.value = None
            senha.value = None
            page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='"Email" ou "Senha" INVÁLIDO'
                ),
                bgcolor='red',
                action='OK',
                duration=3000
            )
            #page.overlay.append(snack_bar)
            #snack_bar.open()
            page.snack_bar.open = True
            page.update()
            pass

        ...

    def btn_cadastro(e):
        try:
            auth.create_user_with_email_and_password(usuario.value, senha.value)
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='Registrado com Sucesso'
                ),
                bgcolor='green',
                action='OK',
                duration=3000
            )
            #page.overlay.append(snack_bar)
            #snack_bar.open()
            page.snack_bar.open = True

            usuario.value = None
            senha.value = None
            page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value='Algo deu Errado'
                ),
                bgcolor='red',
                action='OK',
                duration=3000
            )
            #page.overlay.append(snack_bar)
            #snack_bar.open()
            page.snack_bar.open = True
            page.update()
            pass
        ...



    texto_login = ft.Text(
        value= 'Login',
        size= 32,
        weight= 'bold',
        color= 'white'
    )

    usuario = ft.TextField(
        hint_text= 'Email',
        label= 'Email',
        width=200,
        border_color= 'white',
        color= 'white',
        label_style=ft.TextStyle(
            color= 'white'
        )
    )

    senha = ft.TextField(
        hint_text= 'Senha',
        label= 'Senha',
        width= 200,
        border_color= 'white',
        color= 'white',
        label_style=ft.TextStyle(
            color='white'
        ),
        password=True,
        can_reveal_password=True
    )

    botao_logar = ft.ElevatedButton(
        text= 'Entrar',
        color= 'White',
        bgcolor= 'Black',
        width= 200,
        height= 50,
        on_click=btn_login
    )

    botao_cadastro = ft.ElevatedButton(
        text='Cadastro',
        color='White',
        bgcolor='Black',
        width=200,
        height=50,
        on_click=btn_cadastro
    )

    page.add(
        texto_login,
        usuario,
        senha,
        botao_logar,
        botao_cadastro
    )

ft.app(target=main)

