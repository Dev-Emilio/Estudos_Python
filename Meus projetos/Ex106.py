#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep
c = ('\033[m',        #0 - SEM COR
     '\033[0;30;41m', #1 - VERMELHO
     '\033[0;30;42m', #2 - VERDE
     '\033[0;30;43m', #3 - AMARELO
     '\033[0;30;44m', #4 - AZUL
     '\033[0;30;45m', #5 - ROXO
     '\033[7;40m'    #6 - BRANCO
     )

def ajuda(com):
    titulo(f'ACESSANDO O MANUAL DO COMANDO "{com}"', 3)
    print(c[6], end='')
    help(com)
    print(c[6], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('*' * tam)
    print(f'  {msg}')
    print('*' * tam)
    print(c[0], end='')
    sleep(1)

#Programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 4)
    comando = str(input('FUNÇÃO OU BIBLIOTECA (Digite "fim" para sair) > '))
    if comando.upper() in 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO', 1)