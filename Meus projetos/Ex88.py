#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
lista = []
jogos = []
tot = 1
print('='*20)
print(f'{'JOGO DA MEGA SENA':^20}')
print('='*20)
n = int(input('QUANTOS JOGOS VOCÊ QUER QUE EU SORTEIE? '))
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot +=1
print(f'-=-=-=> SORTEANDO {n} JOGOS <=-=-=-')
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(0.8)
print('-='*4, '> BOA SORTE <', '=-'*4)
