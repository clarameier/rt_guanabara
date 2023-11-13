'''o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do primeiro aluno: '))
a3 = str(input('Digite o nome do primeiro aluno: '))
a4 = str(input('Digite o nome do primeiro aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem da apresentação destes alunos será respectivamente: {lista}')