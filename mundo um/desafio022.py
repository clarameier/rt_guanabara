'''crie um programa que leia o nome completo de uma pessoa e mostre: 1. o nome com todas as letras maiúsculas; 2. o nome com todas minúsculas; 3. quantas letras tem ao todo (sem considerar os espaços); 4. quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: '))

#nome com todas as letras maiúsculas
masc = (nome.upper())
print(f'Seu nome tem em maiúsculo fica deste jeito: {masc}.')
#nome com todas as letras minúsculas
minu = (nome.lower())
print(f'Seu nome tem em minúsculo fica deste jeito: {minu}.')
#quantas letras tem ao todo sem espaços
conta = (len(nome) - nome.count(' '))
print(f'Seu nome tem {conta} letras.')
#quantas letras tem o primeiro nome
primeiro = nome.split()
first = len(primeiro[0])
print(f'Seu primeiro nome tem {first} letras.')

'''ou então poderia fazer assim:
primeiro = nome.find(' ')
print(f'Seu primeiro nome tem {primeiro} letras.')'''