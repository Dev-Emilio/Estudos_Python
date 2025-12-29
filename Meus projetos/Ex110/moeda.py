def aumentar(preco=0, taxa=0, formatacao=False):
    resposta = preco + (preco * taxa/100)
    return resposta if formatacao is False else moeda(resposta)


def diminuir(preco=0, taxa=0, formatacao=False):
    resposta = preco - (preco * taxa/100)
    return resposta if formatacao is False else moeda(resposta)


def dobro(preco=0, formatacao=False):
    resposta = preco * 2
    return resposta if formatacao is False else moeda(resposta)


def metade(preco=0, formatacao=False):
    resposta = preco/2
    return resposta if formatacao is False else moeda(resposta)


def moeda(preco=0, moeda= 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco, aumento, reducao):
    print('='*30)
    print('RESUMO DO VALOR'.center(30))
    print('='*30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco : \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de reducao: \t{diminuir(preco, reducao, True)}')
    print('='*30)