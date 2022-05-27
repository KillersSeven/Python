# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

Vc = float(input('Digite o valor da casa: '))
Vs = float(input('Digite o valor do salário: '))
Qa = int(input('Em quantos anos irá pagar? '))
Meses = Qa * 12
prestacao = Vc / Meses
if prestacao > Vs * 0.30:
    print('Infelizmente seu empréstimo não foi aprovado.')
else:
    print(f'Empréstimo aprovado! Você irá pagar a prestação de {prestacao:.2f}R$ em {Meses}x.')
print('Tenha uma ótima semana.')
