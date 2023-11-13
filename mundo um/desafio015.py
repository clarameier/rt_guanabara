'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.'''

km = float(input('Quantos Km você percorreu com o carro? '))
dias = int(input('E por quantos dias você alugou o carro? '))

valor = (km * 0.15) + (60 * dias)

print(f'Então você deve pagar {valor:.2f} reais pelo uso do carro.')