#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.Ex:escreva(‘Olá, Mundo!’) Saída:~~~~~~~~~Olá, Mundo!~~~~~~~~~
def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


#PROGRAMA PRINCIPAL
escreva('MEU NOME É EMIÍLIO')
escreva('ESTOU ESTUDANDO PYTHON')
escreva('QUERO SER DESENVOLVEDOR DE AUTOMAÇÕES')
escreva('ESSE É UM PEQUENO PROGRAMA UTILIZANDO FUNÇÕES')
escreva('UM DIA ELE SERA UMA IA')