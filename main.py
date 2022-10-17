import PySimpleGUI as sg

from lib.login import Login
from lib.usuario import Usuario


login = Login()
window = login.layout_main()
window['-USUARIO-'].set_focus()

while True:
    event, values = window.read()

    # Dados informados pelo usuário através interface gráfica
    registrar = Usuario(values['-USUARIO-'], values['-SENHAR-'])

    if event in (sg.WINDOW_CLOSED, 'Sair'):
        break
    elif event == 'Cadastrar':
        login.cadastrar(window, registrar)
    elif event == 'Acessar':
        login.acessar(window, registrar)

window.close()
