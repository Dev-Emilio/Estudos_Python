#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
totp = hom = mul = 0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('='*20)
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('SEXO: [M/F] ')).strip().upper()[0]
    if idade <= 20 and sexo == 'F':
        mul += 1
    if idade > 18:
        totp += 1
    if sexo == 'M':
        hom += 1
    print('-'*20)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totp}')
print(f'Ao todo temos {hom} homens cadastrados')
print(f'E temos {mul} mulheres com menos de 20 anos')