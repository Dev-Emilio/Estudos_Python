#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
escolha = randint(0, 10)
contador = 0
acertou = False
print('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
while not acertou:
    palpite = int(input('Qual seu palpite: '))
    contador += 1
    if palpite == escolha:
        acertou = True
    else:
        if palpite < escolha:
            print('Mais... Tente mais uma vez: ')
        else:
            print('Menos... Tente mais uma vez: ')
if contador <=5:
    print('Acertou com {} tentativas. Parabens!'.format(contador))
else:
    print('Acertou com {} tentativas. Você é ruim!'.format(contador))