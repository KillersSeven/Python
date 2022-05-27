# ELabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À vista dinheiro/cheque - 10% de desconto; À vista no cartão - 5% de desconto; Em até 2x no cartão - preço normal; 3x ou mais no cartão - 20% de juros.
print('Vamos calcular o valor do produto!')
Vproduto = float(input('Qual o valor? '))
print('Qual é a forma de pagamento? ')
print('[ 1 ] À vista dinheiro/cheque(10% de desconto)')
print('[ 2 ] À vista cartão de crédito(5% de desconto)')
print('[ 3 } Em até 2x no cartão(valor fica normal sem acréscimo)')
print('[ 4 ] Em 3x ou mais cartão(20% de juros')
opcao = int(input('Qual forma de pagamento?'))
if opcao == 1:
    print(f'O valor à vista no dinheiro/cheque é de{Vproduto - Vproduto*(10/100)}R$.')
elif opcao == 2:
    print(f'O valor à vista no cartão de crédito é de {Vproduto - Vproduto*(5/100)}R$.')
elif opcao == 3:
    print(f'Em até 2x o valor de {Vproduto} não tem acréscimo ou desconto.')
else:
    print(f'Em 3x ou mais o produto recebe 20% de juros.\nEntão o valor com acréscimo é de {Vproduto + Vproduto*(20/100)}R$, gerando parcelas a partir de 3x de {(Vproduto + Vproduto*(20/100))/3}.')


