'''faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. ex: ana maria de souza; primeiro: ana; último = souza.'''

nome = str(input('Digite o seu nome completo, por favor: '))

lista = nome.split()

#primeiro nome
primeiro = lista[0]
print(f'O seu primeiro nome é: {primeiro}.')

#último nome
ultimo = lista[len(lista)-1]  #não entendi bem ainda pq -1 massss ok
print(f'O seu último nome é: {ultimo}.')
