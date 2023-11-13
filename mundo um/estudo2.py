'''MUNDO UM PYTHON GUANABARA'''

#ordem de precedência:
print(5 + 3 * 2)
print(3 * 5 + 4 ** 2)
print(3 * (5+4) ** 2)

#vai centralizar a resposta com '=' antes e depois do nome:
nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer {nome:=^20}!')

#
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1+n2
produto = n1 * n2
divisao = n1 / n2
inteira = n1 // n2
potencia = n1 ** n2

print(f'A soma vale {soma}; o produto vale {produto}; a divisão vale {divisao}; a divisão inteira vale {inteira}; e a potência vale {potencia}.')

'''anotações guanabara:
1. pow() dá o valor de um número elevado de alguma potência
2. colocar \n quebra a linha na frase do código
3. raiz quadrada é: n1 ** (1/2)
4. usando por exemplo :.2f só será apresentado apenas os 2 primeiros digitos da palavra ou número'''