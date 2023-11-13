'''crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. ex: digite um número: 6.127; o número 6.127 tem a parte inteira 6.'''

from math import trunc
num = float(input('Digite um número: '))
inteiro = trunc(num)

print(f'O número inteiro do número escolhido por você é igual a {inteiro}.')
