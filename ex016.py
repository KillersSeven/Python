# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira. Ex: Digite um número: 6.127/O número 6.127 tem a parte inteira 6.
from math import trunc
n1 = float(input('Digite o número Real: '))
print(f'O número {n1} tem sua parte inteira igual a {trunc(n1)}')
