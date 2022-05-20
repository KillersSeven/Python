# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
a1 = str(input('Qual é o nome do primeiro Aluno? '))
a2 = str(input('Qual é o nome do segundo Aluno? '))
a3 = str(input('Qual é o nome do terceiro Aluno? '))
a4 = str(input('Qual é o nome do quarto Aluno? '))
Lista = [a1, a2, a3, a4]
shuffle(Lista)
print(f'A ordem de apresentação será: ')
print(Lista)






