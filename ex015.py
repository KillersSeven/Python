# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
Da = float(input('Quantos dias alugado? '))
Kr = float(input('Quantos Km rodados? '))
CustoDia = Da*60
CustoKM = Kr*0.15
print(f'O total a pagar é {CustoDia+CustoKM:.2f}')
