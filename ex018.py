# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
Ang = float(input('Digite o ângulo: '))
seno = sin(radians(Ang))
print(f'O ângulo de {Ang} tem o SENO de {seno:.2f}')
cosseno = cos(radians(Ang))
print(f'O ângulo de {Ang} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(Ang))
print(f'O ângulo de {Ang} tem a TANGENTE de {tangente:.2f}')


