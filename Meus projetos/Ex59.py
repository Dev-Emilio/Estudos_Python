#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
opcao= 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual sua escolha: '))
    if opcao == 1:
        print('A soma entre {} + {} é {}'.format(p, s, (p+s)))
    elif opcao == 2:
        print('A multiplicação entre {} x {} é {}'.format(p , s, (p*s)))
    elif opcao == 3:
        if p > s:
            maior = p
        else:
            maior = s
        print('Entre {} e {} o maior valor é {}'.format(p, s, maior))
    elif opcao == 4:
        print('Informe os valores novamente: ')
        p = int(input('Primeiro valor: '))
        s = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finzalinando...')
    else:
        print('Opção invalida!!! Por favor digite um numero de 1 a 5')
    print('=-='*6)
    sleep(1)
print('Fim do programa! Volte sempre')
