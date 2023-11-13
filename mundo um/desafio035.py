'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''

r1 = float(input('Digite um número: '))
r2 = float(input('Digite mais um número: '))
r3 = float(input('Digite um último número: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com estes valores, podemos formar um triângulo!')
else:
    print('Com estes valores não podemos formar um triângulo!')