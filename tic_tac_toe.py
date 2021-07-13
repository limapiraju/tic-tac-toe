"""Atualizado em 13-07-2021."""

import random, time


def recebe_jogada(vez_do_jogador):  
    """Implementa entradas de jogada do participante ou do computador.

    vez_do_jogador = bool
    
    Aceita entradas da linha (lin) e da coluna (col) escolhida pelo jogador.
    Testa se valor está entre 1 e 3.
    Retorna esses valores como inteiros.
    """

    # se é a vez do participante
    if vez_do_jogador:

        # linha escolhida
        while True:
            lin = str(input("Digite a linha em que quer jogar: "))
            print("-" * 50)

            # se a jogada é válida
            if lin in ["1", "2", "3"]:
                break
            
            print("Valor inválido!")
            print("-" * 50)

        # coluna escolhida
        while True:
            col = str(input("Digite a coluna em que quer jogar: "))
            print("-" * 50)
            if col in ["1", "2", "3"]:
                break
            print("Valor inválido!")
            print("-" * 50)

        return int(lin), int(col)

    # se é a vez do computador
    else:
        
        while True:
            lin, col = random.randint(1, 3), random.randint(1, 3)
            return lin, col

        

def testa_fim(tabuleiro_estado):
    """Avalia se o jogo chegou ao fim em um dado momento.

    tabuleiro_estado = matriz 3 x 3 (listas aninhadas) representando o atual estado do tabuleiro.
    
    0s representam células vazias.
    1s representam células com jogadas do jogador humano.
    -1s representam células com jogadas do computador.
    Retorna alguem_venceu (None = ninguém venceu, 1 = jogador humano venceu, 0 = computador venceu) e
    jogadas_indisponiveis (True, False).
    """

    alguem_venceu = None
    jogadas_indisponiveis = 1 # será convertido em booleano a seguir
    
    # controla a soma da coluna
    soma_coluna = [0, 0, 0]

    # d1 = diagonal principal; d2 = diagonal secundária
    d1 = d2 = 0 
    
    for i, linha in enumerate(tabuleiro_estado):
        # controla a soma da linha
        soma_linha = 0 

        # Somando valores de linha e de coluna em soma_linha e soma_coluna, respectivamente
        for j, coluna in enumerate(linha):
            soma_linha += coluna
            soma_coluna[j] = soma_coluna[j] + coluna

            # se algum valor em coluna for 0, a multiplicação resultará em 0; logo, jogadas_indisponiveis = False
            jogadas_indisponiveis *= coluna 

            # Teste da diagonal principal
            if i == j:
                d1 += coluna

            # Teste da diagonal secundária
            if i + j == 2:
                d2 += coluna

        # alguem venceu nas linhas?    
        if soma_linha == 3:
            # jogador venceu
            alguem_venceu = 1
            break
        
        elif soma_linha == -3:
            # computador venceu
            alguem_venceu = 0
            break

    # alguem venceu nas colunas?       
    for i in soma_coluna:
        if i == 3:
            # jogador venceu
            alguem_venceu = 1
            break
        
        elif i == -3:
            # computador venceu
            alguem_venceu = 0
            
    # alguem venceu nas diagonais?
    if d1 == 3 or d2 == 3:
        # jogador venceu
        alguem_venceu = 1
        
    elif d1 == -3 or d2 == -3:
        # computador venceu
        alguem_venceu = 0

    return alguem_venceu, jogadas_indisponiveis

  


def testa_jogada(linha, coluna, tabuleiro_estado, vez_do_jogador):
    """Testa a validade da jogada feita pelo jogador.

    Recebe linha e coluna indicadas como jogada, o estado atual do tabuleiro e de quem é a vez:
    - linha: opção de jogada na linha;
    - coluna: opção de jogada na coluna;
    - tabuleiro_estado: estado atual do tabuleiro;
    - vez_do_jogador (bool): True indica que é a vez do jogador humano.

    Checa se jogada é inválida (True) ou não (False).
    Retorna o resultado dessa checagem e o estado do tabuleiro atualizado.
    """

    # Se a opção do tabuleiro já está ocupada
    if tabuleiro_estado[linha - 1][coluna - 1] != 0:
        if vez_do_jogador:
            imprime("Posição inválida! Selecione outra jogada.", antes = False)
            
        return True, tabuleiro_estado

    # se é a vez do jogador humano
    if vez_do_jogador:
        # atualiza célula em que foi feita a jogada
        tabuleiro_estado[linha - 1][coluna - 1] = 1

    # se é a vez do computador
    else:
        # atualiza célula em que foi feita a jogada
        tabuleiro_estado[linha - 1][coluna - 1] = -1
        
    return False, tabuleiro_estado

      

def atualiza_tabuleiro(tabuleiro_estado, simbolo):
    """Atualiza o tabuleiro com os símbolos Xs e Os.

    Recebe as listas aninhadas que representam o atual estado do tabuleiro.
    Parâmetro símbolo informa se participante é X ou O.
    Imprime uma representação desse tabuleiro com símbolos Xs e Os.
    """
    
    # mapeamento do estado de cada casela e de seus respectivos símbolos
    
    tabuleiro_dict = [{0: ' ', 1: 'O', -1: 'X'}, # tabuleiro_dict[0] = participante é "O"
                      {0: ' ', 1: 'X', -1: 'O'}] # tabuleiro_dict[1] = participante é "X"

    
    # imprime o tabuleiro
    print("    1   2   3  ")
    for pos, linha in enumerate(tabuleiro_estado):
        print("  -------------")
        print(pos + 1, end = " ")
        for col in linha:
            print("| {} " .format(tabuleiro_dict[simbolo][col]), end = "")
        print("|")
    print("  -------------")



def jogada(tabuleiro_estado, vez_do_jogador, simbolo):
    """Implementa outras funções relacionadas à jogada.

    Funções implementadas: recebe_jogada(), testa_jogada() e atualiza_tabuleiro()
    Retorna o estado atualizado do tabuleiro.
    """
    jogada_invalida = True

    # enquanto a entrada for uma jogada inválida
    while jogada_invalida: 
        linha, coluna = recebe_jogada(vez_do_jogador)
        jogada_invalida, tabuleiro = testa_jogada(linha, coluna, tabuleiro_estado, vez_do_jogador)
        
    atualiza_tabuleiro(tabuleiro_estado, simbolo)

    return tabuleiro



def imprime(text, antes = True, depois = True):
    """Implementa a função print com umas frescuras antes e depois do texto principal.

    antes (True): imprime hífens antes do texto;
    depois (True): imprime hífens depois do texto.
    """
    
    if antes:
        print("-" * 50)
        
    print(text)

    if depois:
        print("-" * 50)
    


def main():
    """Controla todas as demais funções e implementa o jogo."""

    vez_do_jogador = bool(random.randint(0, 1))

    jogar_novamente = True

    while jogar_novamente:


        # Definindo símbolos
        while True:
            simbolo = input("Com qual símbolo você quer jogar (0 = O, 1 = X)? ")
            if simbolo in ["0", "1"]:
                simbolo = int(simbolo)
                break
            
            imprime("Opção inválida!", antes = False)
            
        # representação do tabuleiro momento a momento
        # 0 = sem jogada
        # 1 = jogada do jogador humano
        # -1 = jogada do computador
        tabuleiro_estado = [[0, 0, 0],
                            [0, 0, 0],
                            [0, 0, 0]]


        # Controlando o jogo      
        while True:

            if vez_do_jogador:
                imprime("Agora é a sua vez de jogar.")
                time.sleep(2)

                tabuleiro_estado = jogada(tabuleiro_estado, vez_do_jogador, simbolo)
                vez_do_jogador = False

            else:
                imprime("Agora é a vez do computador jogar.")
                time.sleep(2)

                imprime("O computador está pensando na jogada...", antes = False)
                time.sleep(2)
                
                tabuleiro_estado = jogada(tabuleiro_estado, vez_do_jogador, simbolo)
                vez_do_jogador = True


            # Testa se jogo chegou ao fim
            vencedor, jogadas_indisponiveis = testa_fim(tabuleiro_estado)

            # Se o tabuleiro está completo e ninguém venceu, jogo empatou
            if jogadas_indisponiveis and vencedor is None:
                imprime("Empatou!")
                break
                
            # se o jogador venceu
            if vencedor == 1:
                imprime("Você venceu!")
                break

            # se o computador venceu            
            elif vencedor == 0:
                imprime("Computador venceu!")
                break
            
        # Controlando o início de um novo jogo
        while True:
            jogar_novamente = str(input("Deseja jogar novamente (S - Sim; N - Não)? ")).lower()[0]
            if jogar_novamente not in ["s", "n"]:
                imprime("Opção inválida! Tente novamente.")

            elif jogar_novamente == "n":
                imprime("Volte sempre!")
                
                jogar_novamente = False
                break
            
            else:
                break
            
    


main()
    
    
    
