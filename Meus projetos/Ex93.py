#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
for c in range (0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Totgols'] = sum(partidas)
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador['Nome']} jogou {len(jogador['Gols'])} partidas')
for i, v in enumerate(jogador['Gols']):
    print(f'    => Na partida {i+1}, fez {v} gols')