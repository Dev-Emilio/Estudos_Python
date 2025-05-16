#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:– Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)
def notas(*n, sit=False):
    '''
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não indicar a situação
    :return: dicionario com varias informações sobrea a situação da turma.
    '''
    aluno = {}
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n)/len(n)
    if sit:
        if aluno['media'] >= 7:
            aluno['situacao'] = 'BOA'
        elif aluno['media'] >= 5:
            aluno['situacao'] = 'RAZOAVEL'
        else:
            aluno['situacao'] = 'RUIM'
    for k, v in aluno.items():
        print(f'{k} é {v}', end=' /// ')
    return aluno



#PROGRAMA PRINCIPAL
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
