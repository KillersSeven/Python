# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
Vi = float(input('Digite a distância da sua viagem em Km: '))
P1 = 0.50
P2 = 0.45
if Vi <= 200:
    print(f'O valor de sua viagem será de: {Vi*P1}R$')
else:
    print(f'O valor de sua viagem será de: {Vi*P2}R$ ')
print('Faça uma ótima viagem!')



