# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float(input('Digite a Largura da Parede: '))
alt = float(input('Digite a Altura da Parede: '))
área = larg*alt
print(f'Sua parede tem a dimensão de {larg}x{alt}, e sua área é de {área}m² ')
tinta = área/2
print(f'A quantidade de tinta necessária para pintar esta parede é de {tinta} litros.')




