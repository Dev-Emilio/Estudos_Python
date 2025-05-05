#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for i in range(0, 3):
        matriz[l] [i] = int(input(f'Digite um valor para [{l}, {i}] na sua matriz matriz: '))
print('='*20)
for l in range (0, 3):
    for i in range (0, 3):
        print(f'[{matriz[l] [i]:^5}]', end='')
    print()