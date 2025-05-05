#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:A) A soma de todos os valores pares digitados.B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = soma = 0
for l in range (0, 3):
    for i in range (0, 3): # LINHAS QUE PREENCHEM A MATRIZ
        matriz[l] [i] = int(input(f'Digite um valor para a posição [{l}, {i}] da sua matriz: '))
print('=-'*20)
for l in range (0, 3): #LINHAS QUE MOSTRAM A MATRIZ
    for i in range (0, 3):
        print(f'[{matriz[l] [i]:^5}]', end='')
        if matriz[l] [i] % 2 ==0:
            pares += matriz[l] [i]
        if i ==2:
            soma += matriz[l][i]
        if l ==1:
            maior = matriz[1][i]
    print()
print('-='*20)
print(f'A soma dos valores pares da matriz é {pares}')
print(f'A soma dos valores da terceira coluna é {soma}')
print(f'O maior valor digitado na segunda linha é {maior}')