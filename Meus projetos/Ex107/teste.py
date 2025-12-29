#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

p = int(input('Digite o preco R$ '))
print(f'A metade de {p} e {moeda.metade(p)}')
print(f'O dobro de {p} e {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 20%, temos {moeda.diminuir(p, 20)}')