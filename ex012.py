# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
Vo = float(input('Qual é o valor total do produto? '))
Vd = Vo*(5/100)
Vf = Vo-Vd
print(f'O valor original do seu produto é de {Vo}, com 5% de desconto seu valor final é de {Vo-Vd}')
