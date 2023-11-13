'''faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².'''

larg = float(input('Qual a largura, em metros, da sua parede? '))
alt = float(input('Qual a altura, em metros, da sua parede? '))

area = larg * alt
tinta = area / 2

print(f'Sua parede tem {area} m² de área. Portanto, será necessário comprar {tinta} litros de tinta.')
