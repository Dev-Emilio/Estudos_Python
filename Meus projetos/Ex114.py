import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim nao esta acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso')