'''um professor que sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.'''

from random import choice

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

lista = [a1, a2, a3, a4]
sorteado = choice(lista)

print(f'O(A) aluno(a) escolhido(a) para apagar o quadro foi: {sorteado}.')
