'''crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

n1 = int(input('Digite um número: '))

dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print(f'O dobro de {n1} é de {dobro}; o triplo é de {triplo}; e a sua raiz quadrada é de {raiz:.2f}.')