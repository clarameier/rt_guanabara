'''faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

valor = float(input('Qual o valor do produto que você deseja? '))
desconto = valor - (valor * 0.05)

print(f'O seu produto, com 5% de desconto passará a custar {desconto:.2f} reais.')