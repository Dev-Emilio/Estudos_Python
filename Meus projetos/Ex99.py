#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep
def maior(*num):
    maior = cont = 0
    print('-='*30)
    print('Analisando os valores passados ...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        elif maior < valor:
            maior =valor
        cont +=1
    print(f'Foram digitados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


#PROGRAMA PRIMCIPAL
maior(2, 9, 4, 5, 7, 1)
maior(4, 7,0)
maior(1, 2)
maior(6)
maior()

