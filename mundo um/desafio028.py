'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import choice

pense = [0, 1, 2, 3, 4, 5]
sorteio = choice(pense)

usuario = int(input('Digite um número de 0 a 5 e lhe diremos se o computador pensou o mesmo: '))
if usuario == sorteio:
    print(f'Parabéns, você acertou, o número escolhido realmente foi {sorteio}!')
else:
    print(f'Poxa você errou, a máquina escolheu o número {sorteio} e não {usuario}.')