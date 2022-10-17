import PySimpleGUI as sg


class Login:

    @staticmethod
    def layout_main():
        sg.set_options(font='_ 10')

        layout = [
            [sg.Titlebar('Login')],
            [sg.VPush()],
            [sg.T('Usuário', s=(6, 1), p=(26, 1)), sg.I(k='-USUARIO-', s=(20, 1)), sg.Push()],
            [sg.T('Senha', s=(6, 1), p=(26, 1)),
             sg.I(k='-SENHAR-', s=(8, 1), justification='c', password_char='*'), sg.Push()],
            [sg.T(' ', p=(26, 1), k='-INFO-'), sg.Push()],
            [sg.Push(), sg.B('Acessar'), sg.B('Cadastrar'), sg.B('Sair'), sg.Push()],
            [sg.VPush()],
        ]

        window = sg.Window('Login', layout, element_justification='r', size=(300, 200), keep_on_top=True, finalize=True)
        return window

    @staticmethod
    def cadastrar(window, registrar):
        # Se não existir cadastro, os dados informados serão validados e salvos
        if registrar.verificar_existencia_cadastro():
            window['-INFO-'].update('Usuário já cadastrado!', text_color='red')
            return False

        # Se o usuário não tiver no mínimo 6 ítens, será informado na cor vermelho
        if not registrar.padronizar_nome():
            window['-INFO-'].update('Usuário deve ter no mínimo 6 ítens', text_color='red')
            return False

        # Se a senha não tiver 6 ítens, será informado na cor vermelho
        if not registrar.criar_hash_senha():
            window['-INFO-'].update('Senha tem que ter 6 ítens', text_color='red')
            return False

        # Passado pelas validações, os dados serão salvos
        registrar.cadastrar()
        window['-INFO-'].update('Cadastro efetuado com sucesso!', text_color='#32CD32')

        # Serão limpos os campos após salvos
        window['-USUARIO-'].update('')
        window['-SENHAR-'].update('')
        window['-USUARIO-'].set_focus()

    @staticmethod
    def acessar(window, registrar):
        # Usuário e senha informado iguais aos dados salvos, efetua o acesso
        if registrar.login():
            window['-INFO-'].update('Login efetuado com sucesso!', text_color='blue')
        else:
            window['-INFO-'].update('Os dados não conferem!', text_color='red')


if __name__ == '__main__':
    pass
