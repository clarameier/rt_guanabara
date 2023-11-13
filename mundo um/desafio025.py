'''crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = str(input('Digite o seu nome: '))
masc = nome.upper()
silva = 'SILVA' in masc
print(f'Seu nome tem Silva? {silva}')