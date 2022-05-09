from random import sample

alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLM'
numeric = '123456789'
special = '!@#$%¨&*?-+._,'


def senha(numero=False, letra=False, especial=False, tamanho=1):
    match numero | letra | especial:

        case True | True | True:
            senha_resultado = alpha + special + numeric
            return f'{sample(senha_resultado, tamanho)}'

        case True | True | False:
            senha_resultado = numeric + alpha
            return sample(senha_resultado, tamanho)

        case True | False | True:
            senha_resultado = numeric + special
            return sample(senha_resultado, tamanho)

        case False | True | True:
            senha_resultado = alpha + special
            return sample(senha_resultado, tamanho)
