#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:A) Quantos números foram digitados.B) A lista de valores, ordenada de forma decrescente.C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True: #forma de fazer a repetição
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break #ponto de parada
print('-='*20)
print(f'A lista em ordem decrescente é {sorted(lista, reverse=True)}')# forma de fazer a lista decrescente
print(f'Você digitou {len(lista)} numeros.')
if 5 in lista:
    print('Você digitou o numero 5 na lista')
else:
    print('Não foi encontrado o numero 5 na lista')
