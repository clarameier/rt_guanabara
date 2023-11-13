'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = float(input('Digite a que velocidade estava o carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f'Por desrespeitar as leis do trânsito, você está sendo multado. Sua multa terá um valor de {multa:.2f} reais.')
else:
    print('Obrigada por respeitar a velocidade delimitada!')