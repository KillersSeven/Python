# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: -Se ele ainda vai se alistar ao serviço militar; -Se é a hora de se alistar; -Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
Idade = int(input('Qual é a sua idade? '))
print('-=-'*30)
print('Iremos analisar seu possível Alistamento Militar.'.center(80))
print('-=-'*30)
if Idade == 18:
    print('Você deve imediatamente se apresentar a junta militar de sua região!')
elif Idade > 18:
    print(f'Seu prazo para alistamento já passou em {Idade-18} anos.')
else:
    print(f'Ainda não é sua hora. Você ainda tem {18-Idade} anos para o seu alistamento.')

