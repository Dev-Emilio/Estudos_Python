#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitoria = 0
print('-='*12)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*12)
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    print('-'*20)
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-'*20)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            vitoria +=1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            vitoria +=1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente?')
print('='*20)
print(f'GAME OVER!!! Você venceu {vitoria} vezes')