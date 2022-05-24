# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Digite a primeira medida: '))
r2 = float(input('Digite a segunda medida: '))
r3 = float(input('Digite a terceira medida: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triângulo!')
else:
    print('Não é um triângulo.')
