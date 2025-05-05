#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Media: '))
print('-='*30)
if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 <= aluno['media']  < 7:
    aluno['situacao'] = 'RECUPERAÇÂO'
else:
    aluno['situacao'] = 'REPROVADO'
for k, v in aluno.items():
    print(f' - {k} é igual {v}')