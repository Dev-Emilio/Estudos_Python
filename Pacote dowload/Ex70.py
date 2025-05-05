#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
totalc = caro = barato = pbarato = cont = 0
print('='*30)
print('      LOJA SUPER BARATAO')
print('='*30)
while True:
    nome = str(input('NOME DO PRODUTO: '))
    valor = float(input('PREÇO: R$ '))
    cont += 1
    totalc += valor
    if valor > 1000:
        caro += 1
    if cont == 1 or valor < pbarato:
        barato = nome
        pbarato = valor
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('{:-^40}'.format(' Fim do programa '))
print(f'O total da compra foi de R$ {totalc:.2f}')
print(f'Temos {caro} produto custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {barato} que custa {pbarato}')
