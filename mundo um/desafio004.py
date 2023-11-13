'''faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

programa = input('Digite algo: ')

classe = type(programa)
numerico = programa.isnumeric()
alfabeto = programa.isalpha()
alnum = programa.isalnum()
masc = programa.isupper()
minu = programa.islower()
space = programa.isspace()
cap = programa.istitle()

print(f'O que você digitou tem a classe {classe}.')
print(f'O que você digitou é númerico? {numerico}.')
print(f'O que você digitou é alfabeto? {alfabeto}.')
print(f'O que você digitou é alphanúmerico? {alnum}.')
print(f'O que você digitou é todo em letras maiúsculas? {masc}.')
print(f'O que você digitou é todo em letras minúsculas? {minu}.')
print(f'O que você digitou só tem espaços? {space}.')
print(f'O que você digitou está capitalizada? {cap}.')