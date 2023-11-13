'''Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

from datetime import date #isto vai importar a data atual

ano = int(input('Digite um ano qualquer, ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #isto vai dizer o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Este é sim um ano bissexto!')
else:
    print('Este não é um ano bissexto!')