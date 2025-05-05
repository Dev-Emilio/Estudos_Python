#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
cadastrop = {}
listap = []
soma = media = 0
while True: #MOMENTO DO LOOP PARA CONTINUAR O PROGRAMA
    cadastrop.clear()
    cadastrop['Nome'] = str(input('NOME: '))
    while True: #VALIDAÇÃO DO SEXO
        cadastrop['Sexo'] = str(input('SEXO: [M/F] ')).strip().upper()[0]
        if cadastrop['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    cadastrop['Idade'] = int(input('IDADE: '))
    soma += cadastrop['Idade']
    listap.append(cadastrop.copy())
    while True: #MOMEMNTO PARA VALIDAÇÃO DA CONTINUAÇÃO
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor digite apenas S ou N.')
    if resp in 'N': #RESPONSAVEL POR PARAR O PROGRAMA
        break
print('-='*20)
print(f'A) Ao todo temos {len(listap)} pessoas cadastradas')
media = soma / len(listap)
print(f'B) A media das idades é {media:5.2f}')
print('C) As mulheres cadastradas foram', end='')
for p in listap:
    if p['Sexo'] in 'Ff':
        print(f'{p["Nome"]} ', end='')
print()
print('D) Lista das pessoas que estão a cima da média: ', end='')
print()
for p in listap:
    if p['Idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('>>> ENCERRANDO <<<')