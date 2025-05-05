#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    for c in range (0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
        jogador['Gols'] = partidas[:]
        jogador['Totgols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp in 'N':
        break
print('-'*40)
for k, v in enumerate(time):
    print(f'')

print('-='*20)
print(f'O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gols')