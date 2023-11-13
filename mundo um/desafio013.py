'''faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario = float(input('Qual o valor do seu salário? '))
aumento = salario + (salario * 0.15)

print(f'Parabéns, você terá um aumento de 15% e o seu salário passará a ser de {aumento} reais.')