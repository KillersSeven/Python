# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - O primeiro valor é maior; -O segundo valor é maior; -Não existe valor maior, os dois são iguais.
Num1 = int(input('Digite o primeiro número: '))
Num2 = int(input('Digite o segundo número: '))
print('-=-'*30)
print('Vamos comparar os dois números escolhidos!'.center(80))
print('-=-'*30)
if Num1 > Num2:
    print('O primeiro valor é maior. ')
elif Num2 > Num1:
    print('O segundo valor é maior. ')
else:
    print('Os valores são equivalentes. ')
print('Tenha um ótimo dia! ')
