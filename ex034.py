# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
Sal = float(input('Qual é o seu salário? '))
S1 = Sal*(10/100)
S2 = Sal*(15/100)
if Sal > 1250:
    print(f'O seu aumento será de 10%, logo... seu salário será de {Sal+S1}R$')
else:
    print(f'O seu aumento será de 10%, logo... seu salário será de {Sal+S2}R$')
print('Parabéns pelo seu aumento!')
