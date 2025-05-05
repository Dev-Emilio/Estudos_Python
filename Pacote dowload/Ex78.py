listanum = []
mai = meno = 0
for c in range (0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = meno = listanum
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < meno:
            meno = listanum[c]
print('='*30)
print(f'Você digitou {listanum}')
print(f'O maior valor digitado foi {mai} nas posições', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {meno} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == meno:
        print(f'{i}...', end='')
print()