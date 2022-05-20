# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
A1 = str(input('Qual é o nome do primeiro aluno? '))
A2 = str(input('Qual é o nome do segundo aluno? '))
A3 = str(input('Qual é o nome do terceiro aluno? '))
A4 = str(input('Qual é o nome do quarto aluno? '))
lista = [A1, A2, A3, A4]
Sorteado = choice(lista)
print(f'O aluno escolhido foi o(a) {Sorteado}!')


