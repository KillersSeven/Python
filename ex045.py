# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('-=-'*30)
print('Bem vindo ao meu Jokenpô!'.center(80))
print('-=-'*30)
computador = randint(0, 2)
print('Você pode escolher primeiro: ')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
jogador = int(input('Qual é a sua jogada? '))
print('Vamos jogar!')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(3)
print('-='*11)
print(f'O computador jogou: {itens[computador]}')
print(f'O jogador jogou: {itens[jogador]}')
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
print('Fim do jogo.')