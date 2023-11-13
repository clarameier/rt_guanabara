'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

numero = int(input('Digite um número: '))
resto = numero % 2
if resto == 0:
    print('Seu número é um número par.')
else:
    print('Seu número é um número ímpar.')