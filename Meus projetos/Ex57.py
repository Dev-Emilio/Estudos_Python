#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
r = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while r not in 'MmFf':
    r = str(input('Dados invalidos. Por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(r))
