#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteia (lista): #FUNÇÃO PARA SORTEAR OS VALORES 
    print('Sorteando 5 valores da lista ', end='')
    for cont in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista): #FUNÇÃO PARA SOMAR OS PARES
    soma = 0
    for valores in lista:
        if valores % 2 ==0:
            soma += valores
    print(f'Somando os valores PARES de {lista} temos {soma}')

#PROGRAMA PRINCIPAL
numeros = list()
sorteia(numeros)
somapar(numeros)