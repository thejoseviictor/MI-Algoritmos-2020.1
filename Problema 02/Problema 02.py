#/*******************************************************************************
# Autor: José Victor de Oliveira Correia
# Componente Curricular: Algoritmos I
# Concluido em: 22/04/2021
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/

# Jogo Asteroids da "Rookie Software Inc".

import keyboard # Ler as teclas pressionadas.
from time import sleep # Dar delay.
import os # Limpar o terminal.
import random # Aleatorizar um dos caracteres do asteroid.
import threading # Vai fazer os procedimentos rodarem simultaneamente com o programa principal.

menu_principal = 0 # Se está variável for igual a "0", o programa irá entrar no menu.

# Está estrutura de repetição é o Menu Principal do jogo.
while menu_principal == 0:
    os.system('cls') # Vai limpar o terminal.
    print('Bem-vindo(a) ao Asteroids')
    print('\nSelecione uma das opções abaixo:')
    print('(1) Jogar\n(2) Recordes\n(3) Sobre\n(4) Sair\n')
    try:
        menu_principal = int(input('Sua escolha: '))
        if menu_principal < 0: # Se o valor digitado for menor que "0", não irá corresponder
                               # a nenhuma opção no menu e retornará ao início do loop.
            os.system('cls')
            print('\nDigite uma opção válida!\n')
            sleep(1)
            menu_principal = 0 # Vai definir o valor "0" a variável e irá retornar ao início do menu principal.
    # Irá tratar os erros, caso o usuário digite uma letra ou nada no menu.
    except (ValueError, TypeError):
        os.system('cls')
        print('\nDigite uma opção válida!\n')
        sleep(1) # Vai esperar 1 segundo antes de retornar ao início do loop.
    
    # Irá iniciar uma nova partida no jogo, caso o usuário escolha a opção "1" no menu. 
    if menu_principal == 1:

        # Este é o plano de fundo inicial do jogo (altura: 15 caracteres, largura: 22 caracteres).
        plano_de_fundo = [['Pontos:',0,' ',' ',' ',' ',' ',' ',' ','Vidas:',10,' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
                          [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
        
        # Estas são as coordenadas iniciais dos caracteres da nave no plano de fundo.
        # A nave tem 04 caracteres.
        nave = {
            'caractere01_linha':12,
            'caractere01_coluna':10,
            'caractere02_linha':13,
            'caractere02_coluna':9,
            'caractere03_linha':13,
            'caractere03_coluna':10,
            'caractere04_linha':13,
            'caractere04_coluna':11,
        }

        # Essa variável será usada para verificar se algum projetil
        # acertou um asteroid. Se ela for verdadeira, pontos serão 
        # acrescentados ao placar do jogador e o asteroid será destruído.
        acertou_asteroid = False

        # Vai ser usada para saber se o fim de jogo foi causado pela destruição da nave.
        nave_destruida = False

        # Procedimento para limpar e imprimir um novo frame na tela.
        def limpar_tela(matriz, limpar): # "Matriz" vai receber o plano de fundo e "Limpar" vai receber uma confirmação, True.
            if limpar == True:
                os.system('cls')
                for linha in range(15):
                    for coluna in range(22):
                        print(matriz[linha][coluna], end='')
                    print('\n')

        # Definindo o procedimento que vai mover a nave no plano de fundo.
        # Ele pega o caractere da nave e o reposiciona à direita ou à esquerda, 
        # em seguida, substitui o caractere do seu local anterior por um espaço 
        # em branco, dando uma ilusão de movimentação.
        def movimentar_nave(matriz, local_nave, tecla):

            # Se a seta da esquerda no teclado for pressionada, os caracteres irão se mover uma coluna para a esquerda.
            if tecla == 'left':
                matriz[local_nave['caractere02_linha']][local_nave['caractere02_coluna']] = ' '
                local_nave['caractere02_coluna'] -= 1
                matriz[local_nave['caractere02_linha']][local_nave['caractere02_coluna']] = '*'

                matriz[local_nave['caractere03_linha']][local_nave['caractere03_coluna']] = ' '
                local_nave['caractere03_coluna'] -= 1
                matriz[local_nave['caractere03_linha']][local_nave['caractere03_coluna']] = '*'

                matriz[local_nave['caractere01_linha']][local_nave['caractere01_coluna']] = ' '
                local_nave['caractere01_coluna'] -= 1
                matriz[local_nave['caractere01_linha']][local_nave['caractere01_coluna']] = '*'

                matriz[local_nave['caractere04_linha']][local_nave['caractere04_coluna']] = ' '
                local_nave['caractere04_coluna'] -= 1
                matriz[local_nave['caractere04_linha']][local_nave['caractere04_coluna']] = '*'
            
            # Se a seta da direita no teclado for pressionada, os caracteres irão se mover uma coluna para a direita.
            if tecla == 'right':
                matriz[local_nave['caractere04_linha']][local_nave['caractere04_coluna']] = ' '
                local_nave['caractere04_coluna'] += 1
                matriz[local_nave['caractere04_linha']][local_nave['caractere04_coluna']] = '*'

                matriz[local_nave['caractere03_linha']][local_nave['caractere03_coluna']] = ' '
                local_nave['caractere03_coluna'] += 1
                matriz[local_nave['caractere03_linha']][local_nave['caractere03_coluna']] = '*'

                matriz[local_nave['caractere01_linha']][local_nave['caractere01_coluna']] = ' '
                local_nave['caractere01_coluna'] += 1
                matriz[local_nave['caractere01_linha']][local_nave['caractere01_coluna']] = '*'

                matriz[local_nave['caractere02_linha']][local_nave['caractere02_coluna']] = ' '
                local_nave['caractere02_coluna'] += 1
                matriz[local_nave['caractere02_linha']][local_nave['caractere02_coluna']] = '*'
        
        # Procedimento que vai criar os projeteis no plano de fundo e somar os pontos.
        # Primeiramente, ele cria manualmente os três caracteres dos projeteis
        # e registra a localização deles no plano de fundo.
        # Em seguida, uma repetição pega os caracteres dos projeteis e os reposiciona
        # para cima, depois substitui o caractere do seu local anterior por um espaço em branco.
        # Por fim, os projeteis são apagados (substituindo-os por espaços em branco), assim que eles
        # rompem os limites do plano de fundo.
        def projeteis(matriz, local_nave, tecla, mostrar_projeteis):
            global acertou_asteroid # Chamando a variável global que afirma se um asteroid foi destuido ou não.
            incremento_pontos = 0 # Incremento dos pontos, que irá aumentar gradualmente
                                  # sempre que um asteroid for destruido.
            if tecla == 'space':
                while mostrar_projeteis == True:
                    # Coordenadas iniciais dos projeteis.
                    projeteis_coluna = nave['caractere01_coluna'] # Surgem sempre acima do primeiro caractere da nave.
                    projetil_01_linha = 9
                    projetil_02_linha = 10
                    projetil_03_linha = 11
                    # Exibindos os primeiros caracteres dos projeteis, até a linha 9 do plano de fundo.
                    matriz[projetil_03_linha][projeteis_coluna] = 'o'
                    sleep(0.1)
                    matriz[projetil_02_linha][projeteis_coluna] = 'o'
                    sleep(0.1)
                    matriz[projetil_01_linha][projeteis_coluna] = 'o'
                    sleep(0.1)
                    for linha in range(8, 0, -1): # Responsável por fazer os projeteis subirem.
                        matriz[linha][projeteis_coluna] = 'o'
                        matriz[linha+3][projeteis_coluna] = ' '
                        sleep(0.1)
                        matriz[linha+1][projeteis_coluna] = 'o'
                        matriz[linha+3][projeteis_coluna] = ' '
                        sleep(0.1)
                        matriz[linha+2][projeteis_coluna] = 'o'
                        matriz[linha+3][projeteis_coluna] = ' '
                        sleep(0.1)
                        # Vai verificar se os projeteis irão colidir com um asteroid,
                        # se sim, os projeteis serão apagados e a variável "acertou_asteroid",
                        # vai dar um sinal ao procedimento do asteroid de que ele precisa ser apagado.
                        # Por fim, os pontos serão somados de acordo com o seu incremento.
                        if matriz[linha-1][projeteis_coluna] == '*':
                            matriz[linha][projeteis_coluna] = ' '
                            matriz[linha+1][projeteis_coluna] = ' '
                            matriz[linha+2][projeteis_coluna] = ' '
                            incremento_pontos += 10 # Vai aumentar em "10" o incremento dos pontos.
                            matriz[0][1] += incremento_pontos # Irá somar os pontos com o incremento.
                            acertou_asteroid = True
                            sleep(1) # Irá esperar um segundo até que outros projeteis surjam.
                            acertou_asteroid = False
                            break # Vai sair do loop que sobe os asteroids.
                        # Vai zerar as vidas e sair da partida se a tecla 'esc' for pressionada.
                        if keyboard.is_pressed('esc'):
                            plano_de_fundo[0][10] = 0
                            mostrar_projeteis = False      

                    for linha in range(3, 0, -1): # Vai apagar os projeteis, assim que eles romperem
                                                  # os limites do plano de fundo.
                        matriz[linha][projeteis_coluna] = ' '
                        sleep(0.1)
                        matriz[linha+1][projeteis_coluna] = ' '
                        sleep(0.1)
                        matriz[linha+2][projeteis_coluna] = ' '
                        sleep(0.1)

        # Procedimento que vai criar os asteroids no plano de fundo.
        # Primeiramente, ele cria manualmente todos caracteres do asteroid.
        # Em seguida, uma repetição pega os caracteres e os reposiciona para baixo,
        # depois substitui o caractere do seu local anterior por um espaço em branco.
        # Dentro dessa repetição, tem uma condição que verifica se o asteroid
        # foi destruido (através do valor booleano na variável "acertou_asteroid"), se sim,
        # ele será destruído.
        # Por fim, o asteroid será apagado (substituindo seus caracteres por espaços em branco)
        # e 1 vida será reduzida da nave, caso ele atinja o limite do plano de fundo.
        def mostrar_asteroids(matriz, local_nave, gerar_asteroides):
            global acertou_asteroid # Chamando a variável global que afirma se um asteroid foi destuido ou não.
            # Entrará no loop, se as vidas forem maiores que "0" e o parametro recebido for "True".
            while gerar_asteroides == True and matriz[0][10] > 0:
                # Vai aleatorizar a coluna do caractere 22 do asteroid,
                # a partir desse caractere os outros irão surgir.
                coluna_aleatoria_asteroid = random.randint(4, 17)
                # Coordenadas iniciais do asteroid.
                local_asteroid = {
                    'caractere1_coluna':coluna_aleatoria_asteroid-1,
                    'caractere2_coluna':coluna_aleatoria_asteroid,
                    'caractere3_coluna':coluna_aleatoria_asteroid+1,
                    'caractere4_coluna':coluna_aleatoria_asteroid-2,
                    'caractere5_coluna':coluna_aleatoria_asteroid-1,
                    'caractere6_coluna':coluna_aleatoria_asteroid,
                    'caractere7_coluna':coluna_aleatoria_asteroid+1,
                    'caractere8_coluna':coluna_aleatoria_asteroid+2,
                    'caractere9_coluna':coluna_aleatoria_asteroid-3,
                    'caractere10_coluna':coluna_aleatoria_asteroid-2,
                    'caractere11_coluna':coluna_aleatoria_asteroid-1,
                    'caractere12_coluna':coluna_aleatoria_asteroid,
                    'caractere13_coluna':coluna_aleatoria_asteroid+1,
                    'caractere14_coluna':coluna_aleatoria_asteroid+2,
                    'caractere15_coluna':coluna_aleatoria_asteroid+3,
                    'caractere16_coluna':coluna_aleatoria_asteroid-2,
                    'caractere17_coluna':coluna_aleatoria_asteroid-1,
                    'caractere18_coluna':coluna_aleatoria_asteroid,
                    'caractere19_coluna':coluna_aleatoria_asteroid+1,
                    'caractere20_coluna':coluna_aleatoria_asteroid+2,
                    'caractere21_coluna':coluna_aleatoria_asteroid-1,
                    'caractere22_coluna':coluna_aleatoria_asteroid,
                    'caractere23_coluna':coluna_aleatoria_asteroid+1,
                }
                # Exibindos os primeiros caracteres do asteroid, até a linha 5 do plano de fundo.
                matriz[1][local_asteroid['caractere21_coluna']] = '*'
                matriz[1][local_asteroid['caractere22_coluna']] = '*'
                matriz[1][local_asteroid['caractere23_coluna']] = '*'
                sleep(0.3) # Vai esperar 3 frações de segundo até exibir a próxima linha de caracteres.
                matriz[1][local_asteroid['caractere16_coluna']] = '*'
                matriz[1][local_asteroid['caractere17_coluna']] = '*'
                matriz[1][local_asteroid['caractere18_coluna']] = '*'
                matriz[1][local_asteroid['caractere19_coluna']] = '*'
                matriz[1][local_asteroid['caractere20_coluna']] = '*'
                matriz[2][local_asteroid['caractere21_coluna']] = '*'
                matriz[2][local_asteroid['caractere22_coluna']] = '*'
                matriz[2][local_asteroid['caractere23_coluna']] = '*'
                sleep(0.3) # Vai esperar 3 frações de segundo até exibir a próxima linha de caracteres.
                matriz[1][local_asteroid['caractere9_coluna']] = '*'
                matriz[1][local_asteroid['caractere10_coluna']] = '*'
                matriz[1][local_asteroid['caractere11_coluna']] = '*'
                matriz[1][local_asteroid['caractere12_coluna']] = '*'
                matriz[1][local_asteroid['caractere13_coluna']] = '*'
                matriz[1][local_asteroid['caractere14_coluna']] = '*'
                matriz[1][local_asteroid['caractere15_coluna']] = '*'
                matriz[2][local_asteroid['caractere16_coluna']] = '*'
                matriz[2][local_asteroid['caractere17_coluna']] = '*'
                matriz[2][local_asteroid['caractere18_coluna']] = '*'
                matriz[2][local_asteroid['caractere19_coluna']] = '*'
                matriz[2][local_asteroid['caractere20_coluna']] = '*'
                matriz[3][local_asteroid['caractere21_coluna']] = '*'
                matriz[3][local_asteroid['caractere22_coluna']] = '*'
                matriz[3][local_asteroid['caractere23_coluna']] = '*'
                sleep(0.3) # Vai esperar 3 frações de segundo até exibir a próxima linha de caracteres.
                matriz[1][local_asteroid['caractere4_coluna']-1] = ' '
                matriz[1][local_asteroid['caractere4_coluna']] = '*'
                matriz[1][local_asteroid['caractere5_coluna']] = '*'
                matriz[1][local_asteroid['caractere6_coluna']] = '*'
                matriz[1][local_asteroid['caractere7_coluna']] = '*'
                matriz[1][local_asteroid['caractere8_coluna']] = '*'
                matriz[1][local_asteroid['caractere8_coluna']+1] = ' '
                matriz[2][local_asteroid['caractere9_coluna']] = '*'
                matriz[2][local_asteroid['caractere10_coluna']] = '*'
                matriz[2][local_asteroid['caractere11_coluna']] = '*'
                matriz[2][local_asteroid['caractere12_coluna']] = '*'
                matriz[2][local_asteroid['caractere13_coluna']] = '*'
                matriz[2][local_asteroid['caractere14_coluna']] = '*'
                matriz[2][local_asteroid['caractere15_coluna']] = '*'
                matriz[3][local_asteroid['caractere16_coluna']] = '*'
                matriz[3][local_asteroid['caractere17_coluna']] = '*'
                matriz[3][local_asteroid['caractere18_coluna']] = '*'
                matriz[3][local_asteroid['caractere19_coluna']] = '*'
                matriz[3][local_asteroid['caractere20_coluna']] = '*'
                matriz[4][local_asteroid['caractere21_coluna']] = '*'
                matriz[4][local_asteroid['caractere22_coluna']] = '*'
                matriz[4][local_asteroid['caractere23_coluna']] = '*'
                sleep(0.3) # Vai esperar 3 frações de segundo até exibir a próxima linha de caracteres.
                matriz[1][local_asteroid['caractere1_coluna']-1] = ' ' 
                matriz[1][local_asteroid['caractere1_coluna']] = '*'
                matriz[1][local_asteroid['caractere2_coluna']] = '*'
                matriz[1][local_asteroid['caractere3_coluna']] = '*'  
                matriz[1][local_asteroid['caractere3_coluna']+1] = ' '        
                matriz[2][local_asteroid['caractere4_coluna']-1] = ' '
                matriz[2][local_asteroid['caractere4_coluna']] = '*'
                matriz[2][local_asteroid['caractere5_coluna']] = '*'
                matriz[2][local_asteroid['caractere6_coluna']] = '*'
                matriz[2][local_asteroid['caractere7_coluna']] = '*'
                matriz[2][local_asteroid['caractere8_coluna']] = '*'
                matriz[2][local_asteroid['caractere8_coluna']+1] = ' '
                matriz[3][local_asteroid['caractere9_coluna']] = '*'
                matriz[3][local_asteroid['caractere10_coluna']] = '*'
                matriz[3][local_asteroid['caractere11_coluna']] = '*'
                matriz[3][local_asteroid['caractere12_coluna']] = '*'
                matriz[3][local_asteroid['caractere13_coluna']] = '*'
                matriz[3][local_asteroid['caractere14_coluna']] = '*'
                matriz[3][local_asteroid['caractere15_coluna']] = '*'
                matriz[4][local_asteroid['caractere16_coluna']] = '*'
                matriz[4][local_asteroid['caractere17_coluna']] = '*'
                matriz[4][local_asteroid['caractere18_coluna']] = '*'
                matriz[4][local_asteroid['caractere19_coluna']] = '*'
                matriz[4][local_asteroid['caractere20_coluna']] = '*'
                matriz[5][local_asteroid['caractere21_coluna']] = '*'
                matriz[5][local_asteroid['caractere22_coluna']] = '*'
                matriz[5][local_asteroid['caractere23_coluna']] = '*'
                sleep(0.3) # Vai esperar 3 frações de segundo até exibir a próxima linha de caracteres.

                # Irá fazer os caracteres do asteroid descerem até o final do plano de fundo.
                for linha_dos_outros in range(5, 14):
                    matriz[linha_dos_outros-4][local_asteroid['caractere1_coluna']] = ' '
                    matriz[linha_dos_outros-4][local_asteroid['caractere2_coluna']] = ' '
                    matriz[linha_dos_outros-4][local_asteroid['caractere3_coluna']] = ' '
                    matriz[linha_dos_outros-3][local_asteroid['caractere1_coluna']-1] = ' '
                    matriz[linha_dos_outros-3][local_asteroid['caractere1_coluna']] = '*'
                    matriz[linha_dos_outros-3][local_asteroid['caractere2_coluna']] = '*'
                    matriz[linha_dos_outros-3][local_asteroid['caractere3_coluna']] = '*'
                    matriz[linha_dos_outros-3][local_asteroid['caractere3_coluna']+1] = ' '      
                    matriz[linha_dos_outros-2][local_asteroid['caractere4_coluna']-1] = ' '
                    matriz[linha_dos_outros-2][local_asteroid['caractere4_coluna']] = '*'
                    matriz[linha_dos_outros-2][local_asteroid['caractere5_coluna']] = '*'
                    matriz[linha_dos_outros-2][local_asteroid['caractere6_coluna']] = '*'
                    matriz[linha_dos_outros-2][local_asteroid['caractere7_coluna']] = '*'
                    matriz[linha_dos_outros-2][local_asteroid['caractere8_coluna']] = '*'
                    matriz[linha_dos_outros-2][local_asteroid['caractere8_coluna']+1] = ' '
                    matriz[linha_dos_outros-1][local_asteroid['caractere9_coluna']] = '*'
                    matriz[linha_dos_outros-1][local_asteroid['caractere10_coluna']] = '*'
                    matriz[linha_dos_outros-1][local_asteroid['caractere11_coluna']] = '*'
                    matriz[linha_dos_outros-1][local_asteroid['caractere12_coluna']] = '*'
                    matriz[linha_dos_outros-1][local_asteroid['caractere13_coluna']] = '*'
                    matriz[linha_dos_outros-1][local_asteroid['caractere14_coluna']] = '*'
                    matriz[linha_dos_outros-1][local_asteroid['caractere15_coluna']] = '*'
                    matriz[linha_dos_outros][local_asteroid['caractere16_coluna']] = '*'
                    matriz[linha_dos_outros][local_asteroid['caractere17_coluna']] = '*'
                    matriz[linha_dos_outros][local_asteroid['caractere18_coluna']] = '*'
                    matriz[linha_dos_outros][local_asteroid['caractere19_coluna']] = '*'
                    matriz[linha_dos_outros][local_asteroid['caractere20_coluna']] = '*'
                    matriz[linha_dos_outros+1][local_asteroid['caractere21_coluna']] = '*'
                    matriz[linha_dos_outros+1][local_asteroid['caractere22_coluna']] = '*'
                    matriz[linha_dos_outros+1][local_asteroid['caractere23_coluna']] = '*'
                    # Irá verificar se o asteroid foi atingido por um projetil,
                    # se sim, ele será destruído. E outro irá surgir.
                    if acertou_asteroid == True:
                        matriz[linha_dos_outros-3][local_asteroid['caractere1_coluna']] = ' '
                        matriz[linha_dos_outros-3][local_asteroid['caractere2_coluna']] = ' '
                        matriz[linha_dos_outros-3][local_asteroid['caractere3_coluna']] = ' '     
                        matriz[linha_dos_outros-2][local_asteroid['caractere4_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere5_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere6_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere7_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere8_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere9_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere10_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere11_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere12_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere13_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere14_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere15_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere16_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere17_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere18_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere19_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere20_coluna']] = ' '
                        matriz[linha_dos_outros+1][local_asteroid['caractere21_coluna']] = ' '
                        matriz[linha_dos_outros+1][local_asteroid['caractere22_coluna']] = ' '
                        matriz[linha_dos_outros+1][local_asteroid['caractere23_coluna']] = ' '
                        break # Vai sair da repetição que faz o asteroid descer.
                    # Irá verificar se o asteroid rompeu os limites do plano de fundo,
                    # se sim, ele será destruído e uma vida será reduzida da nave.
                    if linha_dos_outros+2 == 15:
                        matriz[linha_dos_outros-3][local_asteroid['caractere1_coluna']] = ' '
                        matriz[linha_dos_outros-3][local_asteroid['caractere2_coluna']] = ' '
                        matriz[linha_dos_outros-3][local_asteroid['caractere3_coluna']] = ' '     
                        matriz[linha_dos_outros-2][local_asteroid['caractere4_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere5_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere6_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere7_coluna']] = ' '
                        matriz[linha_dos_outros-2][local_asteroid['caractere8_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere9_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere10_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere11_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere12_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere13_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere14_coluna']] = ' '
                        matriz[linha_dos_outros-1][local_asteroid['caractere15_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere16_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere17_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere18_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere19_coluna']] = ' '
                        matriz[linha_dos_outros][local_asteroid['caractere20_coluna']] = ' '
                        matriz[linha_dos_outros+1][local_asteroid['caractere21_coluna']] = ' '
                        matriz[linha_dos_outros+1][local_asteroid['caractere22_coluna']] = ' '
                        matriz[linha_dos_outros+1][local_asteroid['caractere23_coluna']] = ' '
                        matriz[0][10] -= 1 # Vai reduzir uma vida da nave.
                        break # Vai sair da repetição que faz o asteroid descer.
                    sleep(0.3) # Vai esperar 3 frações de segundo, até que outro asteroid surja.
                
        # Vai limpar o terminal e fazer a primeira impressão do plano de fundo.
        limpar_tela(plano_de_fundo, True)

        # Vai definir um valor booleano indicando que os projeteis
        # ainda não estão aparecendo.
        projeteis_asteroids_on = False

        # Repetição que vai rodar o jogo.
        while plano_de_fundo[0][10] > 0:
            limpar_tela(plano_de_fundo, True) # Vai renderizar os frames por segundo do jogo.

            # Vai zerar as vidas e sair da partida se a tecla 'esc' for pressionada.
            if keyboard.is_pressed('esc'):
                os.system('cls')
                plano_de_fundo[0][10] = 0

            # Vai verificar se o asteroid irá colidir com a nave, se sim
            # a partida será finalizada.
            if plano_de_fundo[11][nave['caractere01_coluna']] == '*':
                nave_destruida = True
                plano_de_fundo[0][10] = 0
            elif plano_de_fundo[12][nave['caractere02_coluna']] == '*':
                nave_destruida = True
                plano_de_fundo[0][10] = 0
            elif plano_de_fundo[12][nave['caractere04_coluna']] == '*':
                nave_destruida = True
                plano_de_fundo[0][10] = 0
            
            # Vai verificar se a seta da esquerda, no teclado, foi pressionada,
            # se sim, irá chamar o procedimento que move a nave.
            if keyboard.is_pressed('left'):
                movimentar_nave(plano_de_fundo, nave, 'left') # O parametro "left" vai dizer que a nave
                                                              # vai para a esquerda.
                # Vai definir os limites de movimentação da nave, dentro do plano de fundo.
                if plano_de_fundo[13][0] == '*' or plano_de_fundo[13][21] == '*':
                    movimentar_nave(plano_de_fundo, nave, 'right')          

            # Vai verificar se a seta da direita, no teclado, foi pressionada,
            # se sim, irá chamar o procedimento que move a nave.
            if keyboard.is_pressed('right'):
                movimentar_nave(plano_de_fundo, nave, 'right') # O parametro "right" vai dizer que a nave
                                                               # vai para a esquerda.
                # Vai definir os limites de movimentação da nave, dentro do plano de fundo.
                if plano_de_fundo[13][0] == '*' or plano_de_fundo[13][21] == '*':
                    movimentar_nave(plano_de_fundo, nave, 'left')

            # Os projeteis e os asteroids irão surgir assim que a tecla 'space' for pressionada.
            if keyboard.is_pressed('space'):
                if projeteis_asteroids_on == False: # Vai verificar se os projeteis já foram invocados antes.
                    # Se os projeteis e os asteroids ainda não tiverem sido invocados,
                    # uma nova tarefa será criada e invocará o procedimento que
                    # é responsável por escrever os projeteis no plano de fundo.
                    executar_projeteis = threading.Thread(target=projeteis, args=(plano_de_fundo, nave, 'space', True))
                    executar_projeteis.start()
                    executar_asteroids = threading.Thread(target=mostrar_asteroids, args=(plano_de_fundo, nave, True))
                    executar_asteroids.start()
                    # Vai dizer que os projeteis e os asteroids já foram invocados, impedindo que eles
                    # sejam invocados novamente (para evitar loop infinitos de tarefas).
                    projeteis_asteroids_on = executar_projeteis.is_alive()
                
        os.system('cls') # Vai limpar a tela.
        
        # Vai verificar se o jogador fez pontos ou se os projeteis e asteroids
        # foram invocados, se uma dessas condições for atendida, o jogador poderá
        # registrar o seu record.
        if plano_de_fundo[0][1] > 0 or projeteis_asteroids_on == True:
            # Vai perguntar o nome do jogador e registrar o seu record.
            digitar_nome = 1 # Essa variável vai permitir a entrada no loop do registro de record.
            while digitar_nome == 1:
                try:
                    # Vai verificar se a nave foi destruida.
                    # Se sim, será exibida uma mensagem afirmando isso.
                    if nave_destruida == True:
                        print('Infelizmente, sua nave foi destruida :-(\n')
                    else:
                        print('Fim de jogo!')
                        print('Suas vidas acabaram :-(\n')
                    nome = str(input('Digite o seu nome: ')) # Vai registrar os dados do jogador em um dicionário.
                    dados_jogador = {
                        'nome':nome,
                        'pontuação':plano_de_fundo[0][1]
                    }
                    digitar_nome = 0 # Esse valor vai fazer o jogo sair do loop de registro de records.
                except TypeError: # Tratamento de erro, caso o usuário digite números no nome.
                    print('Digite apenas letras!')      

        menu_principal = 0 # Vai voltar ao início do menu principal, assim que o jogo terminar.

    # Vai exibir os recordes do jogo, caso o usuário escolha a opção "2" no menu. 
    elif menu_principal == 2:
        tem_recordes = True # Esse valor vai permitir a entrada no loop do menu "Recordes".
        while tem_recordes == True:
            try:
                os.system('cls')
                print('Esses são os recordes registrados:\n')
                print(f"Nome: {dados_jogador['nome']}")
                print(f"Recorde de pontuação: {dados_jogador['pontuação']}")
                sleep(5) # Vai esperar 5 segundos antes de retornar ao menu principal.
                tem_recordes = False # Esse valor vai fazer o jogo sair do loop do sub-menu "Recordes".
                menu_principal = 0 # Essa valor vai fazer o jogo voltar ao início do menu principal.
            except (NameError, KeyError):
                print('Ainda não há recordes registrados!')
                sleep(2) # Vai esperar 5 segundos antes de retornar ao menu principal.
                tem_recordes = False # Esse valor vai fazer o jogo sair do loop do sub-menu "Recordes".
                menu_principal = 0 # Essa valor vai fazer o jogo voltar ao início do menu principal.
    
    # Irá exibir o "Sobre" do jogo, caso o usuário escolha a opção "3" no menu. 
    elif menu_principal == 3:
        os.system('cls')
        print('\nEste jogo foi inspirado no clássico "Asteroids" (1979) da Atari.')
        print('Codificação: José Victor de Oliveira Correia')
        print('Design: José Victor de Oliveira Correia')
        print('© 2021 - Todos os Direitos Reservados\n')
        sleep(5) # Vai esperar 5 segundos antes de retornar ao menu principal.
        menu_principal = 0 # Vai definir o valor "0" a variável e voltar ao menu.

    # Saindo do jogo, caso o usuário escolha a opção "4" no menu.    
    elif menu_principal == 4:
        os.system('cls')
        print('\nAté a próxima!\n')
        menu_principal = -1 # Essa valor vai fazer o jogo sair do menu principal.