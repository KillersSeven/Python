# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import sqrt
CatO = float(input('Digite o valor do Cateto Oposto: '))
CatA = float(input('Digite o valor do Cateto Adjacente: '))
Hipotenusa = sqrt(CatO+CatA)
print(f'O comprimento da Hipotenusa é {Hipotenusa:.2f}')


