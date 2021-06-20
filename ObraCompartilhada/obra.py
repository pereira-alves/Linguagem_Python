from ObraCompartilhada.lib.interface import *
from ObraCompartilhada.lib.historia import *
from ObraCompartilhada.lib.funcoes import *

arqCalc = 'Calc.txt'
if arquivoExiste(arqCalc):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arqCalc)

while True:
    resposta = menu(['Conceito', 'Ferramentas', 'Traçado', 'Suporte', 'Créditos', 'Sair'])
    if resposta ==1:
        while True:
            cabeçalho('Conceito')
            resposta = menu(['O que é concreto', 'Materiais', 'Cuidados', 'Voltar'])
            if resposta == 1:
                historia()
            elif resposta == 2:
                materiais()
            elif resposta == 3:
                cura()
            elif resposta == 4:
                break
    elif resposta ==2:
        print('\n'*100)
        while True:
            cabeçalho('Ferramentas')
            resposta = menu(['Ferramentas elétricas', 'Ferramentas manuais','Voltar'])
            if resposta == 1:
                ferramentasEle()
            elif resposta ==2:
                ferramentasMan()
            elif resposta ==3:
                break
    elif resposta == 3:
        cabeçalho('Traçado')
        while True:
            resposta = menu(['O que é traço de concreto?', 'A importância da dosagem', 'Calculadora', 'Voltar'])
            if resposta == 1:
                tracado()
            elif resposta == 2:
                tracado2()
            elif resposta == 3:
                cabeçalho('CALCULADORA')
                print('Utilizaremos o concreto de resistência 25Mpa que é o \n'
                      'mais utilizado para construções de pequeno porte.\n')
                soma = []
                while True:
                    print('Informe o tamanho da forma que irá receber o concreto: \n')
                    comprimento = leiafloat('Comprimento em metros: [ex: 2.50]')
                    largura = leiafloat('Largura em metros: [ex: 2.50]')
                    altura = leiafloat('Altura em metros: [ex: 2.50]')
                    volume = forma(comprimento, largura, altura)
                    print(f'O volume total é de : {volume:.1f}m³')
                    guardarVolume(arqCalc, volume)
                    resposta2 = leiaint('Deseja cadastrar mais formas ? [1]Sim / [2]Não ')
                    if resposta2 ==1:
                        soma.append(volume)
                        print(linha(15))
                    if resposta2 ==2:
                        soma.append(volume)
                        lerArquivo(arqCalc)
                        break
                soma_volume = sum(soma)
                calConcreto25(soma_volume)
                print(f'Foram informados : {len(soma)} valores')
                print(f'Para um volume total de {soma_volume:.1f}m³ em concreto FCK25')
                limpar(arqCalc)
            elif resposta == 4:
                break
    elif resposta == 4:
        cabeçalho('Eng. Anderson Pereira')
        print('Para um melhor suporte nos contate:\n '
              'E-mail: anderson.aza@gmail.com\n '
              'Celular: (21)996101865')
    elif resposta ==5:
        cabeçalho('CRÉDITOS')
        print('Eng. Anderson Pereira')
        print('Eng. Caldas Branco')
        print('Cimentos Máua')
    elif resposta ==6:
        break
