'''MUNDO UM PYTHON GUANABARA'''

#para o sistema dar uma frase (utiliza as aspas ''):
print('Olá, Mundo')

#para o sistema dar o resultado de uma conta (não utiliza as aspas ''):
print(7+4)

#para o sistema dar os números sem somar (utiliza as aspas separadas ''):
print('7'+'4')

#para o sistema dar uma frase (str) e um número (int) ao mesmo tempo com e sem aspas '':
print('Olá' , 5)

#variáveis e print delas:
nome = 'Maria Clara'
idade = 20
peso = 51.0
print(nome, idade, peso)

#variáveis com input e print:
name = input('Qual é o seu nome? ')
years = input('Quantos anos você tem? ')
weight = input('Qual é o seu peso? ')
print(name, years, weight)

#input e int para SOMAR os números solicitados (sem o int, apenas junta os números):
n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
s = n1 + n2
print(f'A soma entre {n1} e {n2} vale {s}.')

#input e float
n = float(input('Digite um número com vírgula: '))
print(f'O número escolhido foi: {n}.')


'''anotações guanabara:
1. toda variável é um objeto
2. input solicita uma resposta
3. int é para números inteiros e str para palavras
4. usar f{} para colocar a variavel dentro do print de uma vez'
5. int (reais) ex: 7, -4, 0, 9875
6. float (flutuantes) ex: 4,5; 0,076; -15,223; 7,0 (mas no código usamos ponto e não vírgula)
7. bool (bolivianos) ex: True, False
8. str (str) ex: 'Olá', '7.5', "" 
9. (+ adição); (- subtração); (* multiplicação); (/ divisão)
10. (** potência); (// divisão inteira); (% resto da divisão)'''

'''
ordem de precedência:
1. ()
2. **
3. *, /, //, %
4.+, -
'''