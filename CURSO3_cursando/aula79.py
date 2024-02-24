"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao, 'Vitoria', 'A dinossaura'))
print(executa(saudacao, 'O Zeca tá na pista', 'falso Raul'))