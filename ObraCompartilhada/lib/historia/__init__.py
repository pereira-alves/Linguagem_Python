from ObraCompartilhada.lib.interface import *
from ObraCompartilhada.lib.funcoes import *

def historia():
    cabeçalho('O que é Concreto')
    print(' Material plástico, que é moldado de maneira a adquirir\n a forma desejada antes que desenvolva um processo\n '
          'de endurecimento, adquirindo resistência suficiente\n para resistir sozinho aos esforços que o solicitam. ')


def cura():
    cabeçalho('Cuidados')
    print()
    print('--> CURA')
    print()
    print(' Dentre os vários cuidados a serem obervados na obra,\n'
          ' para a obtenção de um bom concreto, situam-se em plano\n'
          ' relevante aqueles que denominamos "cura do concreto" \n'
          ' Entendemos por "cura do concreto" um conjunto de medidas que\n '
          'têm por objetivo evitar a evaporação da água utilizada na\n '
          'mistura do concreto e que deverá reagir com o cimento,\n '
          'hidratando-o. Em climas frios a cura abrange também aquelas\n '
          'medidas de proteção contra o congelamento dessa água.\n'
          'As várias qualidades desejadas num bom concreto são\n'
          ' extremamente favorecidas e até mesmo somente conseguidas\n '
          'através de uma boa cura.\n'
          'Principalmente quando o concreto foi lançado há pouco tempo,\n '
          'é ele muito sensível á ação do sol e do vento que, provocaando\n '
          'a evaporação da água da mistura, impossibilita a plena hidratação\n '
          'do cimento, além de promover um forte aumento no fenômeno da\n '
          'retração, responsável pelo aparecimento de fissuras e trincas\n '
          'o que torna o concreto menos resistente e mais suscetível ao\n '
          'ao ataque de agentes agressivos.')
    print()
    print('-->Resistência à ruptura')
    print()
    print(' Com uma cura adequada, a resistência à ruptura dos concretos\n '
          'é substancialmente favorecida.\n'
          ' Segundo o estudioso Petrucci, as principais conclusões são: \n '
          '- a cura úmida melhora a resistência final;\n '
          '- o ensaio saturado dá valores mais baixos que o ensaio a seco;\n '
          '- é possível recuperar parte da resistência perdida pelo abandono\n '
          'da cura quando está é reiniciada;\n '
          '- para 28 dias existe um acrescimo de cerca de 40% entre a cura\n '
          'ao ar e a cura normal.')
    print()
    print('-->Metodos de cura')
    print()
    print('- Irrigação ou Aspersão de Água Um dos métodos mais simples de \n'
          'proteção do concreto fresco é a utilização continua de irrigação \n'
          'da superficie exposta ou a aspersão de água em intervalos frequentes.\n '
          'Quando só se utiliza a aspersão, deve-se ter precaução para que não \n'
          'ocorra um camento muito profundo, a fim de evitar fadiga superficial \n'
          'devida às dilatações e con pões frequentes, em idades nas quais o \n'
          'concreto ainda não desenvolveu por completo a resistência mecânica.\n\n'
          '- Submersão. E, sem dúvida, o método ideal de cura, só que sua \n'
          'aplicação é inita e em geral nada prática. Pode ser empregado com \n'
          'sucesso em lajes, pisos e imentos em que há grande superfície exposta \n'
          'e quando não há necessidade da utili io da superfície nos primeiros dias.\n\n '
          '- Recobrimento. Muito utilizada em obras é a proteção do concreto com \n'
          'recobrimento para evitar a ação direta do sol e do vento.\n'
          'Esse recobrimento deve ser realizado, preferivelmente, mantendo \n'
          'a umidade, pode utilizar-se, para tal fim, areia, terra, sacos de aniagem \n'
          'rompidos etc. O simples recobrimento com sacos de cimento, tábuas etc.\n'
          ', embora evite a ação direta do Sol e do vento, não impede a evaporação, \n'
          'por absorção, da umidade do concreto pelo ar ambiente, sendo um método \n'
          'muito falho que só deve ser utilizado em casos onde a cura é um \n'
          'aspecto de importência secundária.')


def materiais():
    while True:
        cabeçalho('Materiais')
        resposta = menu(['Cimento', 'Brita', 'Água', 'Voltar'])
        if resposta == 1:
            print('Cimento Portland')
            print()
            print('Cimento Portland é o produto obtido pela pulverização de clinker constituído\n '
                  ' essencialmente de silicatos hidráulicos de cálcio, com uma certa proporção\n'
                  ' de sulfato de cálcio natural, contendo, eventualmente, adições de certas\n '
                  'substâncias que modificam suas propriedades ou facilitam seu emprego.\n '
                  'O clinker é um produto de natureza granulosa, resultante da calcinação\n '
                  'de uma mistura daqueles materiais, conduzida até a temperatura de sua\n '
                  'fusão incipiente.\n'
                  'O mercado nacional dispõe de 8 opções, que atendem aos mais variados tipos de obras.\n '
                  'O cimento Portland comum (CP I) é referência, por suas características e propriedades,\n'
                  ' aos demais tipos básicos de cimento Portland. Esses tipos se diferenciam de acordo\n '
                  'com a proporção de clínquer e sulfatos de cálcio e de adições \n'
                  '(tais como escórias, pozolanas e material carbonático) acrescentadas no processo de\n '
                  'moagem. O material carbonático é conhecido no jargão da indústria como fíler calcário.\n '
                  'Os tipos podem diferir também em função de propriedades intrínsecas, como\n '
                  'alta resistência inicial, a cor branca etc. O próprio Cimento Portland\n '
                  'Comum (CP I) pode conter adição, neste caso, de 1% a 5% de material pozolânico,\n '
                  'escória ou carbonato de cálcio e o restante de clínquer.\n '
                  'Já o CPI-S pode conter de 6% a 10% de material carbonático.\n'
                  'O Cimento Portland Composto (CP II- E, CP II-Z e CP II-F) tem adições de escória,\n '
                  'pozolana e fíler, respectivamente, mas em proporções um pouco maiores que no CP I\n '
                  'e no CP I-S. O Cimento Portland de Alto-Forno (CP III) e o Cimento\n '
                  'Portland Pozolânico (CP IV) contam com proporções maiores de\n '
                  'adições: escória, de 35% a 75% (CP III), e pozolana, de 15% a 50% (CP IV).\n')
            while True:
                resposta = menu(['Cimento Portland Comum (CP I)','Cimento Portland Composto (CP II)', 'Cimento Portland de Alto-Forno (CP III)',
                             'Cimento Portland Pozolânico (CP IV)', 'Cimento Portland de Alta Resistência Inicial (CP V-ARI)',
                             'Cimento Portland Resistente a Sulfatos (RS)', 'Cimento Portland de Baixo Calor de Hidratação (BC)' ,
                             'Cimento Portland Branco (CPB)', 'VOLTAR'])
                if resposta == 1:
                    print('É o cimento mais básico disponível no mercado e é indicado para obras que\n '
                          'não requerem propriedades especiais do cimento. Possui somente o gesso como\n '
                          'aditivo, que faz o papel de retardador de pega, aumentando o tempo de aplicação.\n '
                          'Apresenta alto custo e baixa resistência.\n\n'
                          'CP I - S \n\n'
                          'Possui a mesma composição que o CP I, mas com uma pequena adição de material\n '
                          'pozolânico, o que garante menor permeabilidade ao material.')
                elif resposta == 2:
                    print('CIMENTO PORTLAND COM ADIÇÃO DE ESCÓRIA DE ALTO-FORNO (OU CP II-E)\n\n '
                          'Este cimento possui uma composição intermediária entre os dois anteriores,\n '
                          'pois contém adição de escória granulada de alto-forno e é recomendado para\n '
                          'estruturas que exijam um desprendimento de calor moderadamente lento.\n '
                          'Ele também possui calor de hidratação menor, liberando menos calor quando\n '
                          'em contato com a água.\n\n'
                          'CIMENTO PORTLAND COM ADIÇÃO DE MATERIAL POZOLÂNICO (OU CP II-Z)\n\n'
                          'Apresenta adição de pozolana, proporcionando menor permeabilidade ao\n '
                          'cimento. Portanto, seu uso é indicado para obras subterrâneas ou\n '
                          'que fiquem em constante contato com água.\n\n'
                          'CIMENTO PORTLAND COM ADIÇÃO DE MATERIAL CARBONÁTICO - FÍLER (OU CP II-F)\n\n'
                          'Possui adição de material carbonático em sua composição e é mais resistente e\n '
                          'versátil. É indicado para aplicações gerais, como concreto simples, armado,\n '
                          'pré-moldado ou obras que exijam grande resistência do cimento. Seu uso não\n '
                          'é muito indicado para meios agressivos.\n\n')
                elif resposta == 3:
                    print('CIMENTO PORTLAND DE ALTO-FORNO (OU CP-III)\n\n'
                          'Possui adição de alto teor de escória, podendo chegar até 70% em massa.\n '
                          'Isso garante alta durabilidade, baixo calor de hidratação, alta resistência\n '
                          'à expansão e resistência a sulfatos. É indicado para obras convencionais ou \n'
                          'projetos que apresentem grande agressividade ao cimento como barragens,\n '
                          'fundações de máquinas, pistas de aeroporto, indústrias.\n\n')
                elif resposta == 4:
                    print('CIMENTO PORTLAND POZOLÂNICO (CP-IV)\n\n'
                          'Possui material pozolânico em sua composição, o que confere alta resistência\n '
                          'à compressão ao material e durabilidade. É indicado para obras em que estejam\n '
                          'submetidas a grandes variações de temperatura ou expostas à ação de água\n '
                          'corrente, por ser pouco poroso.\n\n')
                elif resposta == 5:
                    print('CIMENTO PORTLAND DE ALTA RESISTÊNCIA INICIAL (CP V)\n\n'
                          'É um cimento básico, sem aditivos, mas é produzido por um processo de dosagem\n'
                          ' e fabricação do clínquer de forma distinta, com maiores quantidades de calcário\n'
                            ' e argila. Assim, possui alta resistência inicial, isto é, torna-se duro e resistente\n '
                            'em muito menos tempo do que outros modelos. É recomendado para fabricação\n '
                            'de concreto e pré-moldados.\n\n')
                elif resposta == 6:
                    print('CIMENTO PORTLAND RESISTENTE A SULFATOS (RS)\n\n'
                          'Possui aditivos que deixam os cimentos resistentes a sulfatos. Presentes em redes\n '
                          'de esgotos, ambientes industriais e em construções em contato com água do mar.\n\n')
                elif resposta == 7:
                    print('CIMENTO PORTLAND DE BAIXO CALOR DE HIDRATAÇÃO (BC)\n\n'
                    'Possui propriedade de retardar o desprendimento de calor, evitando o aparecimento de\n '
                    'fissuras, aumentando a durabilidade da estrutura e sendo resistente às altas temperaturas.\n\n')
                elif resposta == 8:
                    print('CIMENTO PORTLAND BRANCO (CPB)\n\n'
                          'Sua principal característica é possuir coloração branca, que é atingida pela utilização\n '
                          'de matérias-primas com baixo teor de manganês e ferro e uso de caulim no lugar da argila.\n '
                          'É mais utilizado como rejunte de peças cerâmicas.')
                elif resposta == 9:
                    break
        elif resposta == 2:
            while True:
                resposta = menu(['A Origem da Brita', 'Os tipos de brita', 'Voltar'])
                if resposta == 1:
                    print('Quando rochas duras e maiores, como calcário, gnaisse, basalto e granito, são extraídas por meio\n '
                          'de processos de perfuração ou explosão, seus fragmentos passam pela trituração e peneiramento\n '
                          'industrial. O resultado desse processo é a brita, cujo desempenho dependerá muito das propriedades\n '
                          'geológicas da rocha de origem, como composição química, resistência mecânica, textura e tendência\n '
                          'à degradação. A brita de calcário, por exemplo, não suporta atrito em excesso e pode desgastar\n '
                          'facilmente. Logo, não é recomendada para pavimentos e pisos industriais deve ser substituída por\n '
                          'granito, gnaisse ou basalto. No canteiro de obras, as britas são encomendadas seguindo as\n '
                          'especificações desejadas. Cada um dos tipos pode ser usado separadamente ou em conjunto.')
                elif resposta == 2:
                    while True:
                        resposta = menu(['Pó de brita (malha de até 4,8 mm)', 'Brita 0 ou pedrisco (malha entre 4,8 mm e 9,5 mm)',
                                      'Brita 1 (malha entre 9,5 mm e 19 mm)','Brita 2 (malha entre 19 mm e 25 mm)',
                                     'Brita 3 (malha entre 25 mm e 50 mm)', 'Brita 4 (malha entre 50 mm e 76 mm) e Brita 5 '
                                                                            '(malha entre 76 mm e 100 mm)', 'Voltar'])
                        if resposta == 1:
                            print('Devido à sua textura bastante fina, o pó de brita é fácil de ser moldado e pode ser empregado\n '
                              'em calçadas e asfaltos, na fabricação de pré-moldados e na confecção de argamassa para\n '
                              'assentamento e emboço. O pó de brita também serve como estabilizador de solo na construção\n '
                              'do contrapiso. Desde que bem controlado, o pó de brita deve ser utilizado no concreto paran\n '
                              'aumentar sua resistência.')
                        elif resposta == 2:
                            print('O pedrisco, que também tem dimensões pequenas, é utilizado na produção de vigas e vigotas,\n '
                              'lajes pré-moldadas, blocos de concreto para construção e fundação, além de tubos, bloquetes,\n '
                              'paralelepípedos, manilhas e chapiscos. Também é utilizado em concretos para estruturas com\n '
                              'grande taxa de armação ou de pequena espessura, além de concretos mais fluidos\n '
                              '(concreto auto-adensável).')
                        elif resposta == 3:
                            print('A Brita 1 é a mais usada pelas construtoras e aparece em vários processos de obras de grande\n '
                              'porte, como prédios, pontes e espaços comerciais. Seu tamanho é o dobro da Brita 0,\n '
                              'tornando-a ideal para a fabricação de concreto para colunas, vigas e lajes.')
                        elif resposta == 4:
                            print('Quando há necessidade de um concreto extremamente resistente para construções que precisam\n '
                              'suportar mais peso, a Brita 2 é a mais recomendada. Ela é um dos componentes do concreto\n '
                              'bruto e faz parte das fundações e dos pisos de maior espessura.')
                        elif resposta == 5:
                            print('Por possuir uma dimensão maior, essa brita é pouco usada na fabricação de concreto e aparece\n '
                              'mais em obras de aterramento, instalação de drenos e nivelamento de linhas férreas. Além disso,\n '
                              'é grossa o suficiente para reforçar o subleito de rodovias em que há tráfego intenso.')
                        elif resposta == 6:
                            print('Esses dois tipos de brita, também conhecidos como pedra de mão, possuem aplicações bem\n '
                              'específicas por conta de suas dimensões. Assim como a Brita 3, as britas 4 e 5 também atuam\n '
                              'como reforço de subleitos e lastro ferroviário. Elas podem ser usadas ainda em fossas sépticas,\n '
                              'gabiões, sumidouros, tubulões e Estações de Tratamento de Esgoto (ETEs).')
                        elif resposta ==7:
                            break
                elif resposta == 3:
                    break
        elif resposta == 3:
            print('A água de abastecimento público é adequada para o concreto e já vem sendo utilizada, não necessitando\n '
                  'de ensaio. A água potável que atende a Portaria nº 518 do Ministério da Saúde é considerada dentro dos\n '
                  'padrões exigidos pela norma do ABNT/CB-18 e pode ser utilizada sem restrição para a preparação do concreto.\n '
                  'A água de esgoto, mesmo com tratamento, não é adequada para uso em concreto.')
            print('Quando a água vem de fontes subterrâneas, ou quando é de captação pluvial ou ainda oriunda de processo\n '
                  'residual industrial, pode ser boa para uso do concreto, mas deve ser ensaiada. No caso de água salobra\n '
                  '(água com salinidade entre a da água do mar e as chamadas águas doces) também pode ser utilizada,\n '
                  'mas SOMENTE no concreto NÃO ARMADO. Em ambos os casos, segundo a norma, a água deve ser ENSAIADA.\n '
                  'A ÁGUA DO MAR NÃO DEVE SER USADA em concreto armado ou protendido.')
        elif resposta == 4:
            break


def ferramentasEle():
    while True:
        resposta = menu(['Betoneira', 'Vibrador de concreto', 'Voltar'])
        if resposta == 1:
            print('Betoneiras são misturadores de materiais. Existem diferentes tipos e tamanhos. No entanto, a mais\n '
                  'usual é a betoneira de 400 litros, também conhecida como de uma (01) massada. Uma massada\n '
                  '(traço1:3:3) produz aproximadamente 160 litros de concreto, ou seja, 0,16 m3.')
        elif resposta == 2:
            print('O vibrador de concreto é uma ferramenta muito importante na construção civil. Este equipamento é\n '
                  'utilizado para garantir que as estruturas de concreto não tenham bolhas, espaços vazios ou excesso\n '
                  'de água, problemas que podem comprometer a qualidade da estrutura e de toda a obra. Evitar esses\n '
                  'problemas é fundamental: quanto mais vazios, bolhas ou espaço existirem em uma estrutura de concreto,\n '
                  'menor será sua resistência, ocasionando problemas graves na construção. ')
        elif resposta == 3:
            break


def ferramentasMan():
    while True:
        resposta = menu(['Pá/Enxada', 'Balde/Latão/Carrinho de mão','Caixote','Padiola','Voltar'])
        if resposta == 1:
            print('A pá é uma ferramenta manual com uma lâmina, que pode ser reta ou levemente inclinada, para corte.\n '
                  'A lâmina é acoplada na parte inferior de um cabo de madeira.\n '
                  'A enxada é uma ferramenta manual dotada de uma lâmina transversal, acoplada a um cabo de madeira,\n '
                  'que serve basicamente para capinar, mas pode ser utilizada para serviços em obras, como misturar argamassa.')
        elif resposta ==2:
            print('Os baldes de obra são utilizados para o transporte de materiais e alguns casos como dosadores,\n '
                  'no mercado são encontrados em plástico ou em chapa de aço em varios tamanhos, em obra o mais utilizado\n '
                  'é o de 12L.')
            print('Na construção civil , o termo "Lata" é utilizado para designar o volume de uma lata de 18 litros.\n '
                  'Na confecção de concreto ou argamassa, em obra, é normal a utilização da lata para a dosagem de\n '
                  'areia, brita, água e cimento no traço.\n'
                  'O volume de 1m³ equivale a aproximadamente 55,5 latas.')
            print('Existem no mercado de construção civil diversos tipos e modelos de Carrinho de Mão. Todos voltados\n '
                  'para facilitar o trabalho nos canteiros de obras. Dentro os tipos poderemos citar os três modelos mais utilizados:\n\n'
                  'Carrinho de Mão com caçamba plástica\n '
                  'Carrinho de Mão Reforçado com caçamba de aço\n '
                  'Carrinho de Mão tipo Girica com duas rodas\n '
                  'O mais comum em obras são os carrinhos reforçados com caçamba de aço, geralmente de 50L.\n'
                  'O volume de 1m³ equivale a aproximadamente 20 carrinhos.')
        elif resposta ==3:
            print('Caixote para Massa é uma ferramenta de grande utilidade para qualquer pedreiro, ou quem\n '
                  'queira trabalhar com cimento em pequenas, médias e até grandes obras. O melhor uso do caixote para\n '
                  'massa é poder ter uma quantidade mais precisa de concreto sem desperdício e risco de "contaminação"\n '
                  'do concreto. ')
        elif resposta == 4:
            print('As padiolas são caixotes criados em madeira para utilização em dosagem de materias como areia e brita\n '
                  'a padiola contem 4 alças que facilitam no transporte e despejo dos materias dentro de betoneiras. As\n '
                  'padiolas podem variar de tamanho conforme a necessidade do concreto, esse fator será determinado\n '
                  'no intuito de alcançar a resistência do concreto (FCK) solicitada em projetos estruturais')
        elif resposta == 5:
            break

def tracado():
    print('O traço nada mais é do que a indicação da quantidade dos materiais que constituem o concreto.\n '
      'Ele mostra a quantidade de areia e de brita que devem ser usadas na mistura para uma unidade de\n '
      'cimento. Um traço de 1:2:3, por exemplo, indica que a proporção será de 1 parte de cimento por 2\n '
      'partes de areia e 3 partes de brita, sempre obedecendo essa ordem. Já a quantidade correta de água\n '
      'varia porque depende da umidade da areia e da trabalhabilidade final do concreto.\n\n'
      'Em uma obra, a dosagem do concreto pode ser feita de forma prática ou racional. O primeiro modo é\n '
      'medido em volume e baseia-se apenas na experiência do profissional técnico. Por isso, é indicado\n '
      'para concretos de resistência moderada que serão empregados principalmente em pequenas construções.\n '
      'Já a dosagem racional, medida em massa, é exercida por concreteiras especializadas que atendem\n '
      'obras de médio a grande porte. A mistura é feita com rigor para seguir uma série de especificações\n '
      'simultaneamente.')


def tracado2():
    print('O traço deve ser respeitado à risca porque é justamente a proporção entre seus materiais que\n '
      'garantirá certas características fundamentais ao concreto, como resistência, durabilidade e\n '
      'trabalhabilidade. Se isso não acontece corretamente, toda a segurança de uma estrutura pode\n '
      'ser comprometida. \n\n'
      'Assim como existem diferentes tipos de concreto ideais para cada obra, também existem diversos tipos\n '
      'de traço. A proporção muda de acordo com o fim: lajes, contrapisos, muros, fundações, calçadas,\n '
      'vigas etc. Isto é: tudo dependerá dos objetivos para a construção e das\n '
      'particularidades que ela apresenta. Para efeito de calculo, utilizaremos a tabala do Eng. Caldas Branco\n '
      'traçado nº 4 para concreto de 25Mpa após 28 dias de cura.')
