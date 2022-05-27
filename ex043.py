# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5 - abaixo do peso; Entre 18.5 e 25 - Peso ideal; 25 até 30 - Sobrepeso; 30 até 40 - Obesidade; Acima de 40 - Obesidade Mórbida.
print('Vamos verificar seu IMC.')
Peso = float(input('Qual é o seu peso? '))
Altura = float(input('Qual é a sua altura? '))
imc = Peso/(Altura*Altura)
print(f'Seu imc é de {imc:.2f}kg/m²')
if imc < 18.5:
    print('Você está abaixo do Peso.')
elif 25 > imc <= 18.5:
    print('Você está no Peso ideal.')
elif 30 > imc <= 25:
    print('Você está com sobrepeso.')
elif 40 > imc <= 30:
    print('Você está com Obesidade.')
else:
    print('Você está com Obesidade mórbida.')