#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome= '<desconhecido>', gol= 0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato')


#PROGRAMA PRINCIPAL
jogador = str(input('Nomde do jogador: '))
ngol = str(input('Numero de gols: '))
if ngol.isnumeric():
    ngol = int(ngol)
else:
    ngol = 0
if jogador.strip() == '':
    ficha(gol=ngol)
else:
    ficha(jogador,ngol)