'''faça um programa que leia uma frase pelo teclado e mostre: 1. quantas vezes aparece a letra "A'; 2. em que posição ela aparece a primeira vez; 3. em que posição ela aparece a última vez.'''

frase = str(input('Digite algo: ')).strip() #para excluir os caracteres da contagem

#quantidades de letras A
a = frase.upper().count('A')
print(f'A letra "a" aparece {a} vezes.')

#posição que aparece a primeira vez
um = frase.upper().find('A')
print(f'A primeira letra "a" aparece na posição {um +1}.')

#posição que aparece o último a
fim = frase.upper().rfind('A') #rfind é para ÚLTIMA POSIÇÃO
print(f'A última aparição da letra "a" é na posição {fim +1}.')
