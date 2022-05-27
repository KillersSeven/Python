# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: -Média abaixo de 5.0 - Reprovado; -Média entre 5.0 e 6.9 - Recuperação; -Média 7.0 ou superior = Aprovado.
Nota1 = float(input('Digite a primeira nota: '))
Nota2 = float(input('Digite a segunda nota: '))
media = (Nota1+Nota2)/2
print(f'Sua média foi {media}')
if media < 5.0:
    print('Você infelizmente está reprovado.')
elif 7 > media >= 5:
    print('Você está de recuperação')
else:
    print('Você está aprovado!')
