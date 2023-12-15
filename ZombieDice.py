# NOME: FERNANDA TEIXEIRA DE ANDRADE
# CURSO: Tecnologia em Análise e Desenv. de Sistemas - EAD

from time import sleep


def pegarDadoVerde():
    '''
    Dado Verde
    :return: Faces do dado Verde
    '''
    return ('C', 'P', 'C', 'T', 'P', 'C')


def pegarDadoAmarelo():
    '''
    Dado Amarelo
    :return: Faces do dado Amarelo
    '''
    return ('T', 'P', 'C', 'T', 'P', 'C')


def pegarDadoVermelho():
    '''
    Dado Vermelho
    :return: Faces do dado Vermelho
    '''
    return ('T', 'P', 'T', 'C', 'P', 'T')

def initDadosCopo():
    '''
    Colocar todos os 13 dado no copo
    :return: copo com 13 dados
    '''
    copo = []
    for i in range(0, 6):
        copo.append(pegarDadoVerde())
    for i in range(0, 4):
        copo.append(pegarDadoAmarelo())
    for i in range(0, 3):
        copo.append(pegarDadoVermelho())
    return copo


def PegarDadosCopo(copo):
    '''
    Sorteia e tira 3 dados que estão dentro do copo.
    :param copo:
    :return: os 3 dados sorteados e o copo com a quantidade de dados que sabrou.
    '''
    rodadadadosorteado = []
    for i in range(0, 3):
        if len(copo) >= 3:
            numsorteado = randint(0, len(copo) - 1)
            dadosorteado = copo[numsorteado]
            rodadadadosorteado.append(dadosorteado)
            del copo[numsorteado]
        else:
            print('Você não possui dados dentro do copo para continuar a rodada.')
    return rodadadadosorteado, copo


def MostrarDadosCopo(copo):
    '''
    Mostra os dados que estão dentro do copo
    :param copo: Array contendo os dados que estão no copo
    :return: Imprime na tela a cor dos dados que estão no copo
    '''
    coresdadoscopo = []
    for dado in copo:
        if dado == pegarDadoVerde():
            coresdadoscopo.append('VERDE')
        elif dado == pegarDadoAmarelo():
            coresdadoscopo.append('AMARELO')
        else:
            coresdadoscopo.append('VERMELHO')
    print(coresdadoscopo)

def MostrarDadosSorteados(dadosorteado):
    '''
    Mostra os dados que foram sorteados
    :param dadosorteado: Array contendo os dados sorteados
    :return: Imprime na tela a cor dos dados que foram sorteados
    '''
    rodadadadosorteado = []
    for dado in dadosorteado:
        if dado == pegarDadoVerde():
            rodadadadosorteado.append('VERDE')
        elif dado == pegarDadoAmarelo():
            rodadadadosorteado.append('AMARELO')
        else:
            rodadadadosorteado.append('VERMELHO')
    for i in rodadadadosorteado:
        print(i + ', ', end=' ')
    print()


def RodarDado(dado):
    '''
    Randomiza um dado sorteado para saber qual face vai cair
    :param dado: dado que foi sorteado
    :return: face do dado sorteado
    '''
    facedado = dado[randint(0, len(dado) -1)]
    return facedado

# Introdução do jogo/regra
print('-=-' * 20)
print('ZombieDice')
print('-=-' * 20)
sleep(1)
print('Este jogo inclui estas regras, 13 dados e um tubo\n'
      'para guardá-los. Você precisa marcar seus pontos de\n'
      'alguma maneira. Dois ou mais jogadores podem jogar.')
print('-=-' * 20)
sleep(2)
comecar = 0
numerojogadores =0
# Pergunta para começar o jogo
while comecar != 'S':
    comecar = str(input('Você está pronto para começar [S/N]? ')).upper().strip()[0]
    if comecar == 'S':
        while numerojogadores < 2:
            # Mensagem para solicitar o número de jogadores
            try:
                numerojogadores = (int(input('Informe o número de jogadores: ')))
                print('-=-' * 20)
                if numerojogadores > 1:
                # Mensagem para solicitar o nome do jogador
                    print('Qual o nome dos jogadores?')
                # Lista com nome dos jogadores
                    listajogadores = []
                # Lista contagem dos pontos
                    pontosjogadaCGeral = []
                    pontosjogadorC = []
                    pontosjogadorT = []
                    pontosjogadorP = []
                    for nj in range(1, numerojogadores + 1):
                        nomejogador = str(input('Nome do Jogador {}: '.format(nj)))
                        listajogadores.append(nomejogador)
                        pontosjogadaCGeral.append(0)
                        pontosjogadorC.append(0)
                        pontosjogadorT.append(0)
                        pontosjogadorP.append(0)
                elif numerojogadores <= 1:
            # Mensagem para informar que é necessário no mínimo dois jogadores
                    print("O jogo precisa de no mínimo dois jogadores!!!\n")
            except:
                print('Não entendi sua resposta.')
    elif comecar == 'N':
        print('Volte quando estiver preparado!')

# Mensagem para informar o nome do jogador.
print('Os jogadores são: {}'.format(listajogadores))
print('-=-' * 20)
sleep(2)

# Mensagem de como funciona o jogo
print('No seu turno, agite o tubo e pegue 3 dado. Role os dados.\n'
      'Cada um deles representa uma pobre vítima a ser atacada.\n'
      'Os dados vermelhos são os mais difíceis. Os verdes são os\n'
      'mais fáceis e os amrelos são médios.\n'
      'Os dados possuem 3 símbolos:\n'
      'C ➨ Cérebros\n'
      'P ➨ Passos\n'
      'T ➨ Tiro\n')
print('-=-' * 20)
sleep(2)
print('Cérebros ➨ Você devorou o cérebro de sua vítima.')
print()
print('Passos ➨ Sua vítima escapou. Se você escolher rolar dados\n'
      'novamente, você cai re-rolar esses dados, juntamente com\n'
      'novos dados suficientes para rolar 3 sempre.')
print()
print('Tiro ➨ Sua vítima revidou. Se tiver 3 dados com a face de\n'
      'tiro virada para cima, em qualquer momento, seu turno acabou.\n'
      'Caso contrário, você pode optar por parar e marcar pontos ou\n'
      'continuar')
print('-=-' * 20)
sleep(4)
print('Se você escolher continuar, pegue mais três dados, você vai\n'
      'rolar três por vez. Depois de pegar novos dados, você não pode\n'
      'decidir parar...você tem que rolar')
print()
print('Jogue até alguém chegar a 13 Cérebros. Termine a  rodada, todos\n'
      'devem jogar o mesmo número de turnos. Quem tiver devorado mais\n'
      'Cérebros até o final dessa rodada é o vencedor.')
sleep(4)
from random import randint

jogadoratual = 0
dadosorteado = []
confirmacao = ''
#Colocar todos os dados dentro do copo
copo = initDadosCopo()
#Iniciar o jogo
while confirmacao != 'NoiPSdr':
    #Mostrar qual jogador vai jogar e total de cerebros do jogador
    print('***' * 20)
    print(f'Rodado do(a) jogador(a): {listajogadores[jogadoratual]}.'
          f'\nTotal de Cérebros {pontosjogadaCGeral[jogadoratual]}.')
    print('***' * 20)
    sleep(1)
    #Mostrar os dados que tem dentro do copo
    print('+++' * 50)
    print('Dados Dentro do Tubo:')
    MostrarDadosCopo(copo)
    print('+++' * 50)
    #Pedir confirmaçao para sortear os dados e as faces
    confirmacao = input(str('Digite algo para sortear e rodar os dados: '))


    print('+++' * 20)
    sleep(2)
    listadadosorteados = []
    #Sortear, tirar e mostrar 3 dados que estão dentro do copo.
    listadadosorteados, copo = PegarDadosCopo(copo)
    MostrarDadosSorteados(listadadosorteados)
    listafacedado = []
    #Rodar e mostrar a face dos 3 dados sorteados.
    for dado in listadadosorteados:
        facedado = RodarDado(dado)
        listafacedado.append(facedado)
    voltarDadoPassosParaCopo = []
    #Contagem dos pontos da rodada. E voltar o dado com a face passos para o copo.
    for i in range(0, len(listafacedado)):
        if listafacedado[i] == 'C':
            pontosjogadorC[jogadoratual] += 1
        elif listafacedado[i] == 'T':
            pontosjogadorT[jogadoratual] += 1
        elif listafacedado[i] == 'P':
            pontosjogadorP[jogadoratual] += 1
            copo.append(listadadosorteados[i])
    print('{}, {}, {}.'.format(listafacedado[0], listafacedado[1], listafacedado[2]))
    print('Cérebro: {}, Tiro: {}, Passos: {}.'.format(pontosjogadorC[jogadoratual], pontosjogadorT[jogadoratual],
                                                      pontosjogadorP[jogadoratual]))

    # Quando o jogador leva três tiros em uma rodada
    if pontosjogadorT[jogadoratual] >= 3:
        print(f'Você levou 3 ou mais tiros. Perdeu os cérebros desta rodada e a vez de jogar.'
              f'\nQuantidade de cérebros perdidos: {pontosjogadorC[jogadoratual]}.'
              f'\nQuantidade total de cérebros: {pontosjogadaCGeral[jogadoratual]}')
        pontosjogadorC[jogadoratual] = 0
        pontosjogadorP[jogadoratual] = 0
        pontosjogadorT[jogadoratual] = 0

        if jogadoratual >= len(listajogadores) - 1:
            jogadoratual = 0
        else:
            jogadoratual += 1
        copo = initDadosCopo()
    #Condição de vitória
    elif pontosjogadaCGeral[jogadoratual] + pontosjogadorC[jogadoratual] >= 13:
        print(f'O jogador {listajogadores[jogadoratual]} comeu 13 cérebros e ganhou o jogo.')
        break
    else:
        # Pergunta se deseja continuar
        continuar = ''
        while continuar != 'N' and continuar != 'S':
            continuar = input(str('Você deseja continuar[S/N]? ')).upper().strip()[0]
            if continuar == 'S':
                print('---' * 20)
                print('Continuar')
                print('---' * 20)
            # Zerar os tiros e passos se o jogador não quiser continuar na rodada
            elif continuar == 'N':
                pontosjogadaCGeral[jogadoratual] += pontosjogadorC[jogadoratual]
                pontosjogadorC[jogadoratual] = 0
                pontosjogadorP[jogadoratual] = 0
                pontosjogadorT[jogadoratual] = 0
                print(f'Total de Cérebros {pontosjogadaCGeral[jogadoratual]} do jogador {listajogadores[jogadoratual]}')

                if jogadoratual >= len(listajogadores) - 1:
                    jogadoratual = 0
                else:
                    jogadoratual += 1
                copo = initDadosCopo()
                # Mensagem para o próximo jogador
                print('-=-' * 20)
                print('Próximo jogador(a): {}.'.format(listajogadores[jogadoratual]))
                print('-=-' * 20)
            else:
                print('Valor inválido!')
