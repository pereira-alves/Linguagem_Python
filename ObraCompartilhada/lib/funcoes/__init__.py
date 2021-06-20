from ObraCompartilhada.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('VOLUMES INFORMADOS')
        for key, value in enumerate(a):
            dado = value.split(';')
            dado[0] = dado[0].replace('\n', '')
            print(f' \033[31m{dado[0]:>10} m³ de concreto\033[m')
    finally:
        a.close()


def guardarVolume(arq, volume):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{volume:.2f};\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo volume de {volume:.1f}m³ adicionado.')
            a.close()

def limpar(arc):
    open(arc, 'w').close()


def forma(comprimento, largura, altura):
    volume = comprimento*largura*altura
    return volume


def calConcreto25(volume2):
    cimentoKg = volume2*361.9
    cimentoSaco = cimentoKg/50
    areiaMcub = volume2*0.625
    areiaLata = areiaMcub/0.016938
    britaMcub = volume2*0.625
    britaLata = britaMcub/0.018
    aguaL = volume2*208.5
    aguaLata = aguaL/17.375
    cabeçalho('Total em Latas de 18L')
    print(f'Areia úmida = {areiaLata:.1f} Latas')
    print(f'Brita 1 = {britaLata:.1f} Latas')
    print(f'Saco de cimento = {cimentoSaco:.1f} saco de cimento')
    print(f'Água = {aguaLata:.1f} Latas')
