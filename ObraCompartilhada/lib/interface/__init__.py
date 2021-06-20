def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def menu(lista):
    cabeçalho('OBRA COMPARTILHADA !!! CONCRETO !!!')
    c = 1
    for item in lista:
        print(f'\033[33m{c} \033[m- \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mDigite uma opção: \033[m')
    return opc


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0:31mERRO, por favor digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuario optou por não digitar um valor!')
            return 0
        else:
            return n

def leiafloat(msg):
    válido=False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0:31mERRO: \"{entrada}\" é um valor inválido!\033[m')
        else:
            válido = True
            return float(entrada)


def linha(tam=50):
    return '~' * tam
