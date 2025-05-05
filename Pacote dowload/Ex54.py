#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
ma = 0
me = 0
ano = date.today().year
for c in range(1, 8):
    a = int(input('Em que ano nasceu a {}° pessoa: '.format(c)))
    idade = ano - a
    if idade <= 18:
        me += 1
    else:
        ma += 1
print('''Ao todo tivemos {} pessoas maiores de idade
E também tivemos {} pessoas menores de idade'''.format(ma, me))