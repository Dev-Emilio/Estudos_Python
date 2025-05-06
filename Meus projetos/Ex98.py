#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2c) uma contagem personalizada
from time import sleep
def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('-='*18)
    print(f'Contagem de {inicio} ate {fim} de {passo} em {passo}')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.3)
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.3)
        print('FIM')


#PROGRAMA PRINCIPAL
contador(0, 10, 1)
contador(10, 0, 1)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)