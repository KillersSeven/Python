# Faça um programa que leia uma frase pelo teclado e mostre: 1) Quantas vezes aparece a letra "A"; 2) Em que posição ela aparece a primeira vez; 3) Em que posição ela aparece a última vez.
frase = str(input('Diga uma frase: '))
Letra = frase.count('')
print(f'A letra a aparece {frase.count("a")} vezes')
print(f'A letra a aparece primeiro na posição {frase.find("a")+1}')
print(f'E sua ultima posição é: {frase.rfind("a")+1}')




