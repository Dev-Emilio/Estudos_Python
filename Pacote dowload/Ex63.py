#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
print('-'*22)
print('SEQUENCIA DE FIBONACCI')
print('-'*22)
termos = int(input('Quantos termos da sequencia gostaria de ver? '))
t1 = 0
t2 = 1
print('*'*30)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM DA SEQUENCIA')
print('*'*30)