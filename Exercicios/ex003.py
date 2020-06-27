""" Ex.003 - Crei um programa que **leia** dois números e mostre a **soma** entre eles. """
print('{:=^60}'.format(' DESAFIO 003 '))
print('Digite dois números para calcular a soma.')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('O resultado da soma entre {} e {} é: {}'.format(n1, n2, s))