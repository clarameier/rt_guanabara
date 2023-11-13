'''MUNDO UM GUANABARA'''

tempo = int(input('Quantos anos tem seu carro? '))

#podemos fazer assim separado ou
'''if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')'''
#assim tudo junto numa linha
print('carro novo' if tempo <=3 else 'carro velho')

#######
nome = str(input('Qual é o seu nome? '))
if nome == 'Maria Clara':
    print('Eu também me chamo Maria Clara!')
else:
    print('Seu nome é legal!')
print(f'Prazer lhe conhecer, {nome}.')


#########
n1 = float(input('Digite a primeira nota: '))
n2= float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
if m >= 6.0:
    print('Sua média foi boa. Parabéns!')
else:
    print('Sua média não está boa o suficiente, estude mais!')