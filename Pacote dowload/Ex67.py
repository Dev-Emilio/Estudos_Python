#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
nomepro = 'MAQUINA DE TABUADAS'
print(f'{nomepro:=^40}')
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*20)
    if n <= 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c:2} = {n*c}')
    print('-'*20)
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')