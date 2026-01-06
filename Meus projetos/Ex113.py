#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(msg):
    while True:
        try:
            resposta = int(input(msg))
        except ValueError:
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
            continue
        else:
            return resposta

def leiaReal(msg):
    while True:
        try:
            resposta = float(input(msg))
        except ValueError:
            print('\033[0;31mErro! Digite um numero inteiro valido.\033[m')
            continue
        else:
            return resposta



#Programa principal
n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaReal('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')