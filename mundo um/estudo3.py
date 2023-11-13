'''MUNDO UM PYTHON GUANABARA'''

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.floor(raiz)}.')

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz}.')

import emoji
print(emoji.emojize('Olá, mundo! :thumbs_up:'))

'''anotações:
1. módulo é uma biblioteca;
2. ceil (arredonda pra cima); floor (arredonda pra baixo); trunc (elimina vírgula e deixa só o primeiro número); pow (potência); sqrt (raiz quadrada); factorial (fatores);
3. "import math" importa a biblioteca inteira;
4. "from math import sqrt" importa somente o "sqrt" da biblioteca "math".
5. hypot (hipotenusa); sen (seno); cos (cosseno); tan (tangente); radians (converte para graus radianos);
6. a lista é para juntar os dados que queremos e vamos usar
7. biblioteca random é de sorteios (choice é para escolher 1); (shuffle é para sortear todos da lista em alguma ordem)'''