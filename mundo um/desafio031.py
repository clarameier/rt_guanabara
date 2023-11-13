'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.'''

distancia = float(input('Qual a distância da sua viagem, em Km? '))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print(f'Sua passagem tem um total de {passagem:.2f} reais.')