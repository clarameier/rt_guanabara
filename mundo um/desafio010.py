'''crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos doláres ela pode comprar. considere U$1,00 = R$3,27.'''

dinheiro = float(input('Quanto de dinheiro você atualmente tem: '))
dolar = dinheiro / 3.27

print(f'Considerando que o dólar vale 3,27, você consegue comprar {dolar} doláres.')

