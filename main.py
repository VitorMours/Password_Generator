# Bibliotecas 
import PySimpleGUI as sg
from machine import gerador


# Variáveis de Ambiente
sg.theme('TealMono')

# Layout da Janela Base
layout_base = [
    [sg.Text('Escolhas os parâmetros que você deseja para a sua senha abaixo:')],
    [sg.Text('Tamanho'), sg.Input(key="pass_size")],
    [sg.Text('Escolha oque deseja:')],
    [sg.Checkbox('Letras', default=False, key="letters_state"), 
     sg.Checkbox('Números', default=False, key="numbers_state"),
     sg.Checkbox('Caracteres Especiais', default=False, key="special_state")],
    [sg.Button('Gerar Senha')]]

# Layout Janela de Recebimento
password_layout = [
    [sg.Text(f'Sua senha foi gerada com sucesso, tendo em mente que ela tem: {values["pass_size"]} caracteres de tamanho')],
    [sg.Button('Gerar Nova Senha'), sg.Button('Fechar')]
    ]

window_default = sg.Window('Gerador Automático de Senhas', layout_base)
password_window = sg.Window('Gerador de Senha executado com sucesso!', password_layout)


def main():
    while True:
        event, values = window_default.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
            print(event, values)
        elif event == 'Gerar Senha':
            if values["letters_state"] == True and values["special_state"] == True and values['numbers_state'] == True:
                print('Todos os elementos estilísticos foram escolhidos')
            
            elif values["letters_state"] != False and values["special_state"] != False and values['numbers_state'] != False:
                print(2)
            
                
            
            else:
                print('Nenhum elemento estilístico foi escolhido, logo a senha será vazia, ou inexistente...')
            
            
            print(event, values)
            window_default.close()
            result_window()
    window_default.close()


def result_window(values['pass_size']):
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
