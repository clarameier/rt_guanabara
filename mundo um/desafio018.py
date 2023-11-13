'''faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

import math
angulo = int(input('Digite um valor: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O seno de {angulo} é igual a {seno:.2f}, o cosseno igual a {cosseno:.2f} e a tangente igual a {tangente:.2f}.')