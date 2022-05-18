import PySimpleGUI as sg

sg.theme('Dark Amber')

main_layout = [
[sg.Text('Escolhas os atributos desejados abaixo: ')],
[sg.Checkbox('Letras'), sg.Checkbox('Números'), sg.Checkbox('Símbolos Especiais')],
[sg.Text('Digite a quantidade de caracteres: '), sg.InputText()],
[sg.Button('Gerar Senha'), sg.Button('Cancel')]
]

pass_layout = [
    [sg.Text('Senha gerada!')],
    [sg.Button('Voltar'), sg.Button('Fechar')]
]



main_window = sg.Window('Bem-vindo ao Gerador de senhas!', main_layout)
pass_window = sg.Window('Gerador de senhas utilizado', pass_layout)



def main():
    while True:
        event, values = main_window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            print(values)
            main_window.close()
            break
        elif event == 'Gerar Senha':
            main_window.close()
            password()


def password():
    while True:
        # TODO consertar essa parte, diz que está tentando ler uma janela que já seta fechada
        event, values = pass_window.read()
    
        if event == 'Voltar':
            pass_window.close()
            main()
    
        elif event == 'Fechar':
            pass_window.close()
            break



main()
main_window.close()