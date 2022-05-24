# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
Vel = float(input('Marque a velocidade em Km/h: '))

multa = (Vel - 80)*7

if Vel > 80:
    print(f'Você foi multado em {multa}RS')
else:
    print('Parabéns! Você é um motorista consciente e não foi multado.')
print('Seja responsável no Trânsito.')
