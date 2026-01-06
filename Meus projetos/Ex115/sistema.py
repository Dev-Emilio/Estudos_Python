from Ex115.lib.interface import *
from time import sleep

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        cabecalho('Opção 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Opção 3')
    elif resposta == 4:
        cabecalho('Saindo do sistema ... Volte sempre')
        break
    else:
        cabecalho('\033[31mERRO!!! Digite uma opção valida\033[m')
    sleep(1)
