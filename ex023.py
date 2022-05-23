# Faça um programa que leia o número de 0 a 9999 e mostre na tela cada um dos dígitos separados. Ex: Digite um número: 1834 ---> Unidade: 4. Dezena: 3. Centena: 8. Milhar: 1
num = str(input('Digite um número: '))
print(f'A unidade é: {num[3:4]}')
print(f'A Dezena é: {num[2:3]}')
print(f'A Centena é: {num[1:2]} ')
print(f'O Milhar é: {num[:1]}')










