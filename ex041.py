# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos - Mirim; Até 14 anos - Infantil; Até 19 anos - Junior; Até 20 anos - Sênior; Acima: Master.
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nascimento: '))
idade = atual - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('O atleta é mirim.')
elif idade <= 14:
    print('O atleta é Infantil.')
elif idade <= 19:
    print('O atleta é Junior.')
elif idade <= 20:
    print('O atleta é Sênior.')
else:
    print('O atleta é Master.')
