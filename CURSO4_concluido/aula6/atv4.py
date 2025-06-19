'''
Exercício 4: Funções de Agregação

Crie um array NumPy 1D com 10 números aleatórios entre 0 e 1. (Dica:
use np.random.rand()).

Calcule e imprima:

a) A soma de todos os elementos.
b) A média dos elementos.
c) O valor mínimo no array.
d) O valor máximo no array.
e) O desvio padrão (standard deviation) dos elementos.'''


import numpy as np
import math
import statistics

arr_aleatorio = np.random.rand(10)
soma_elementos = np.sum(arr_aleatorio)
media_elementos = np.mean(arr_aleatorio)
min_elemento = np.min(arr_aleatorio)
max_elemento = np.max(arr_aleatorio)
desvio_padrao = np.std(arr_aleatorio)

print(f'\nArray aleatorio:\n{arr_aleatorio}\n')
print(f'Soma dos elementos: {soma_elementos:.2f}')
print(f'Média do elementos: {media_elementos:.2f}')
print(f'Valor minimo: {min_elemento:.2f}')
print(f'Valor máximo: {max_elemento:.2f}')
print(f'Desvio padrão: {desvio_padrao:.2f}')