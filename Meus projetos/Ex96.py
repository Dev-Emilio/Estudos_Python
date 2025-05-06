#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area(largura, comprimento):
    area = largura * comprimento
    print(f'A area de um terreno {largura} x {comprimento} é de {area}')


#programa principal
print(' CONTROLE DE TERRENO')
print('>', '-'*18, '<')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)