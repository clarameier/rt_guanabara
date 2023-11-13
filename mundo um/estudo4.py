'''MUNDO UM GUANABARA'''

frase = 'Curso em Vídeo Python'
print(frase) #mostra a frase toda
print(frase[3]) #mosta apenas o valor na posição 3 (começando a contagem do zero)
print(frase[3:13]) #mostra apenas os valores nas posições a partir do primeiro número e até um número antes do último número indicado
print(frase[:13]) #mostra desde o início até um número antes do último número indicado
print(frase[13:]) #mostra apenas os valores nas posições a partir do primeiro número até o final
print(frase[1:15:2]) #mostra a partir do primeiro valor indicado e terminar de mostrar até o segundo valor indicado, por fim o terceiro valor indicado é a de quantas em quantas vezes haverá um corte
print(frase[1::2]) #mostra a partir do primeiro valor indicado e vai até o final, e o último número indica de quantas em quantas vezes haverá um corte
print(frase[::2]) #mostra desde o ínicio até o fim, e o último número indica de quantas em quantas vezes haverá um corte

print(frase.count('o')) #ele irá contar quantas vezes aparece o valor pedido
print(frase.upper()) #ele irá passar tudo para o maiúsculo
print(frase.upper().count('O')) #ele irá passar tudo para o maiúsculo e depois contar quantas vezes aparece o valor pedido
print(len(frase)) #ele irá contar a quantidade de caracteres (incluindo espaço) tem na sua frase
print(len(frase.strip())) #ele irá contar a quantidade de caracteres MENOS os espaçamentos de ANTES e DEPOIS da sua frase, os espaços DENTRO da frase continuaram a ser contados
print(frase.replace('Python', 'Android')) #ele irá substituir o valor indicado pelo novo valor também indicado
print('Curso' in frase) #ele dirá se o valor indicado existe mesmo ou não na sua frase
print(frase.find('Curso')) #ele dirá a posição em que se encontra o valor indicado (dirá apenas a posição da primeira letra, e se não existir o valor na frase colocará "-1")
print(frase.lower().find('vídeo')) #ele irá repassar tudo para o minúsculo e depois dirá em que posição se encontra o valor indicado
print(frase.split()) #ele irá criar uma lista com todos os valores da frase
