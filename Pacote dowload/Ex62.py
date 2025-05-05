#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('=+='*5)
n1 = int(input('Primeiro termo: '))
n2 = int(input('Qual a razão: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais !=0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += n2
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você gostaria de ver? '))
print('Progressão finalizada com sucesso visualizado {} termos'.format(total))