#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
resp = 'S'
cont = maior = media = soma = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
media = (soma / cont)
print('Você digitou {} numeros e a media foi {}.'. format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))