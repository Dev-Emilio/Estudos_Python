#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['Ctps'] = int(input('Carteira de trabalho (DIGITE 0 SE NÃO TIVER): '))
if cadastro['Ctps'] != 0:
    cadastro['Contratacao'] = int(input('Ano de contratação: '))
    cadastro['Salario'] = float(input('Salário: '))
    cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratacao'] + 35) - datetime.now().year)
print('-='*20)
for k, v in cadastro.items():
    print(f'    - {k} tem o valor {v} ')
