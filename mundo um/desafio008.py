'''escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.'''

metros = float(input('Digite um valor em metros: '))

cent = metros * 100
mili = metros * 1000

print(f'{metros} metros, equivalem a {cent} centímetros e a {mili} milímetros.')