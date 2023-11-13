'''faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.'''

from math import hypot
oposto = float(input('Digite o valor do cateto oposto do triângulo: '))
adjacente = float(input('Digite o valor do cateto adjacente do triângulo: '))

hipotenusa = hypot(oposto, adjacente)

print(f'A hipotenusa dos valores escolhidos por você deu um total de {hipotenusa:.2f}.')