# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
So = float(input('Qual é o seu salário atual? '))
Va = So*(15/100)
Sf = So+Va
print(f'Seu salário de {So} recebeu reajuste de 15%. Seu novo salário é de {Sf}')
