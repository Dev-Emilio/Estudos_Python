#Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado1. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.from Ex111.utilidadescev import moeda
from Ex112.utilidadescev import moeda
from Ex112.utilidadescev import dado1

p = dado1.leiadinheiro('Digite o preco: R$')
moeda.resumo(p, 80, 35)