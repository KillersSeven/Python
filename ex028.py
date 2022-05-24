# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('Vou pensar em um número, tente adivinhar!'.center(80))
Número = int(input('Digite um valor: '))
print('Estou analisando seu número...')
sleep(3)
Escolhido = randint(0, 5)
if Número == Escolhido:
    print('Parabéns!')
else:
    print('Errou!')
