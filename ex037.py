# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: -1 para binário; -2 para octal; -3 para hexadecimal.
Num = int(input('Digite o número inteiro: '))
print('Escolha a base de conversão: ')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXAGONAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{Num} convertido para BINÁRIO é igual a {bin(Num)[2:]}')
elif opção == 2:
    print(f'{Num} convertido para OCTAL é igual a {oct(Num)[2:]}')
elif opção == 3:
    print(f'{Num} convertido para HEXAGONAL é igual a {hex(Num)[2:]}')
else:
    print('Opção inválida. Tente Novamente. ')
