# Crie um programa que leia o nome completo de uma pessoa e mostre: 1) O nome com todas as letras maiúsculas; 2) O nome com todas as letras minúsculas; 3)Quantas letras ao t0do(sem considerar os espaços; 4) Quantas letras tem o primeiro nome.
nome = str(input('Insira seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()})')
print(f'Seu nome em minúsculas é {nome.lower()})')
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras!')
print(f'Seu primeiro nome tem {nome.find(" ")} letras!')











