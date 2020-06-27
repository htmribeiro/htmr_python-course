""" #### Desafio 004
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. (utilizando os métodos "is") """

print('{:=^60}'.format(' DESAFIO 004 '))

n = input('Digite algo: ')

print(f'O tipo primitivo de ({n}) é: {type(n)}')
print(f'O conteúdo ({n}) só tem espaço? {n.isspace()}')
print(f'O conteúdo ({n}) é um número? {n.isnumeric()}')
print(f'O conteúdo ({n}) é alfabético? {n.isalpha()}')
print(f'O conteúdo ({n}) é alfanumérico? {n.isalnum()}')
print(f'O conteúdo ({n}) está em maiúsculas? {n.isupper()}')
print(f'O conteúdo ({n}) está em minúsculas? {n.islower()}')
print(f'O conteúdo ({n}) está capitalizada? {n.istitle()}')