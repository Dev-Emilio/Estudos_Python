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
    return f'{moeda}{preco:.2f}'.replace('.', ',')
