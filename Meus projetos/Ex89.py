#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
cadastro = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    media = (nota1 + nota2)/2
    cadastro.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('='*20)
print(f'{'n°':<4}{'NOME':<10}{'MEDIA':>8} ')
print('='*20)
for i, a in enumerate(cadastro):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('='*20)
    ver = int(input('Mostrar nota de qual aluno? 999 para parar '))
    if ver <= len(cadastro) - 1:
        print(f'As notas de {cadastro[ver][0]} são {cadastro[ver][1]}')
    if ver == 999:
        print('FINALIZANDO...')
        break
print('>>> VOLTE SEMRPRE <<<')