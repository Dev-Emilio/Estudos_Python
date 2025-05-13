#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(nasc):
    from datetime import date
    anoat = date.today().year
    idade = anoat - nasc
    if idade >= 18:
        return f'Você tem {idade} por isso o voto é OBRIGATÓRIO'
    elif idade < 16:
        return f'Você tem {idade} por isso o voto é NEGADO'
    if 16 <= idade <= 18:
        return f'Você tem {idade} por isso o voto é FACULTATIVO'


#PROGRAMA PRINCIPAL
born = int(input('Em que ano você nasceu? '))
print(voto(born))