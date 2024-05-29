# Crie um programa que faça o computador jogar Jokenpô com você.
#_______________________________________________________________
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
computador =  randint (0, 4)
print (''' Suas opções:
       [ 0 ] PEDRA
       [ 1 ] PAPEL
       [ 2 ] TESOURA
       [ 3 ] LAGARTO
       [ 4 ] SPOCK''')
jogador = int(input ('Qual é a sua jogada? '))
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
print ('-=' * 15)
print ('Computador jogou {}'.format(itens [computador]))
print ('Jogador jogou {}'.format(itens [jogador]))
print( '-=' * 15)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print (' JOGADOR VENCEU, PAPEL COBRE PEDRA !')
    elif jogador == 2:
        print ('COMPUTADOR VENCEU, PEDRA AMASSA TESOURA !')
    elif jogador == 3:
        print ('COMPUTADOR VENCEU, PEDRA ESMAGA LAGARTO !')
    elif jogador == 4:
        print ('JOGADOR VENCEU, SPOCK VAPORIZA PEDRA !')
    else:
        print(' JOGADA INVÁLIDA !')


elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print(' COMPUTADOR VENCEU, PAPEL COBRE PEDRA ! ')
    elif jogador == 1:
        print ('EMPATE')
    elif jogador == 2:
        print ('JOGADOR VENCEU, TESOURA CORTA PAPEL !')
    elif jogador == 3:
        print('JOGADOR VENCEU, LAGARTO COME PAPEL ! ')
    elif jogador == 4:
        print (' COMPUTADOR VENCEU, PAPEL REFUTA SPOCK !')
    else:
        print(' JOGADA INVÁLIDA !')


elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU, PEDRA AMASSA TESOURA !')
    elif jogador == 1:
        print('COMPUTADOR VENCEU, TESOURA CORTA PAPEL !')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 3:
        print('COMPUTADOR VENCEU, TESOURA DECAPITA LAGARTO !')
    elif jogador == 4:
        print('JOGADOR VENCEU, SPOCK QUEBRA TESOURA !')
    else:
        print('JOGADA INVÁLIDA !')

    
elif computador == 3: # computador jogou LAGARTO
    if jogador == 0:
        print(' JOGADOR VENCEU, PEDRA ESMAGA LAGARTO !')
    elif jogador == 1:
        print('COMPUTADOR VENCEU, LAGARTO COME PAPEL !')
    elif jogador == 2:
        print(' JOGADOR VENCEU, TESOURA DECAPITA LAGARTO !')
    elif jogador == 3:
        print('EMPATE')
    elif jogador == 4:
        print ('COMPUTADOR VENCEU, LAGARTO ENVENENA SPOCK !')
    else:
        print('JOGADA INVÁLIDA !')


elif computador == 4: # computador jogou SPOCK
    if jogador == 0:
        print(' COMPUTADOR VENCEU, SPOCK VAPORIZA PEDRA !')
    elif jogador == 1:
        print(' JOGADOR VENCEU, PAPEL REFUTA SPOCK !')
    elif jogador == 2:
        print(' COMPUTADOR VENCEU, SPOCK QUEBRA TESOURA !')
    elif jogador == 3:
        print(' JOGADOR VENCEU, LAGARTO ENVENENA SPOCK !')
    elif jogador == 4:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA !')

