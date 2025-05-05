#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
listanum = []
while True:
    n = int(input('Digite um numero: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso...')
    resp = str(input('Quer continuar? [S/N] ' )).strip().upper()[0]
    if resp == 'N':
        break
print(f'Os valores na sua lista são {sorted(listanum)}')