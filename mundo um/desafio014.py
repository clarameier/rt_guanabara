'''Escreva um programa que converta uma temperatua digitada em °C e converta para °F.'''

celsius = float(input('Quantos graus celsius fazem? '))
fahren = (celsius * 1.8) + 32

print(f'A temperatura de {celsius}°C convertida é de {fahren}°F.')