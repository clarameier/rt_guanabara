'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

a = int(input('Digite um número: '))
b = int(input('Digite um segundo número: '))
c = int(input('Digite um terceiro número: '))

#menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#maior
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor número é {menor} e o maior número é {maior}.')