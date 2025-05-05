#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maiorpes = 0
menorpes = 0
for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maiorpes = peso
        menorpes = peso
    else:
        if peso > maiorpes:
            maiorpes = peso
        else:
            menorpes = peso
print('O maior peso lido foi {}KG'.format(maiorpes))
print('O menor peso lido foi {}KG'.format(menorpes))
