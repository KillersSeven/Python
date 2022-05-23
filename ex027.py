# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente. Ex: Ana Maria de Souza; primeiro = Ana, último = Souza.
n = str(input('Digite o nome completo: '))
nome = n.split()
print(f'Muito prazer em te conhecer, {n}!')
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu ultimo nome é: {nome[-1]}')


