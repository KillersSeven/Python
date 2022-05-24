# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from calendar import isleap
Ano = int(input('Digite o ano: '))

if isleap(Ano):
    print('Ele é Bissexto.')
else:
    print('Ele não é Bissexto.')
