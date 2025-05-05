#Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
totaln = [[],[]]
valor = 0
for c in range (1, 8):
    valor = int(input(f'Digite o {c}° numero: '))
    if valor % 2 ==0:
        totaln[0].append(valor)
    else:
        totaln[1].append(valor)
print('-='*24)
print(f'Os valores pares digitados foram {sorted(totaln[0])}')
print(f'Os valores impares digitados foram {sorted(totaln[1])}')