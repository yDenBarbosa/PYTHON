# Desafio com 'Stes'

'''
Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Listal = Funcionários que tem carro e trabalham a noite
Lista2 = Funcionários que tem carro e trabalham durante o dia
Lista3 = Funcionários que não tem carro
'''

funcionarios = ['ANA', 'MARCOS', 'ALICE', 'PEDRO', 'SOPHIA', 'BRUNO', 'MELISSA']
turno_dia = ['ANA', 'MARCOS', 'ALICE', 'MELISSA']
turno_noite = ['PEDRO', 'SOPHIA', 'BRUNO']
tem_carro = ['MARCOS', 'ALICE', 'BRUNO', 'MELISSA']

#lISTA1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

#LISTA2
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

#LISTA3
lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
