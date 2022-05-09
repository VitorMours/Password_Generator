import PySimpleGUI as sg
from machine import gerador

sg.theme('TealMono')

layout_base = [
    [sg.Text('Escolhas os parâmetros que você deseja para a sua senha abaixo:')],
    [sg.Text('Tamanho'), sg.InputText()],
    [sg.Text('Escolha oque deseja:')],
    [sg.Checkbox('Letras', default=False), sg.Checkbox('Números', default=False),
     sg.Checkbox('Caracteres Especiais', default=False)],
    [sg.Button('Gerar Senha')]]

lb_l = layout_base[3][0]
lb_n = layout_base[3][1]
lb_e = layout_base[3][2]
lb_t = layout_base[1][1]

password_layout = [
    [sg.Text('Sua senha foi gerada com sucesso, tendo em mente que ela tem:')],
    [sg.Text(f'{layout_base[1][1]}caracteres de tamanho')],
    [sg.Button('Gerar Nova Senha'), sg.Button('Fechar')]
    #[sg.Text(f'A sua senha é: {gerador.senha(numero=bool(lb_n),letra=bool(lb_l),especial=bool(lb_e),tamanho=lb_t)}')]
    ]

window_default = sg.Window('Gerador Automático de Senhas', layout_base)
password_window = sg.Window('Gerador de Senha executado com sucesso!', password_layout)


def main():
    while True:
        event, values = window_default.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Gerar Senha':
            window_default.close()
            result_window()
    window_default.close()


def result_window():
    while True:
        event, values = password_window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Gerar Nova Senha':
            password_window.close()
            main()

        elif event == 'Fechar':
            password_window.close()


if __name__ == '__main__':
    main()
