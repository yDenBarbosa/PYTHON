'''
Exerccio 1 -Criação e Atributos de Arrays

Crie um array NumPy a partir de uma lista Python [10, 20, 30, 40, 50, 60].

Em seguida, imprima:

a) O array criado.
b) A forma (shape) do array.
c) O tipo de dados (dtype) dos elementos do array.
d) O número de dimensões (ndim) do array.
e) O número total de elementos (size) no array.'''

import numpy as np


list = np.array([10,20,30,40,50,60])
print(f'Array criado: {list}')
print(f'forma do array: {list.shape}')
print(f'tipo de dados dos elementos do array: {list.dtype}')
print(f'O numero de dimensões do array: {list.ndim}')
print(f'O numero total de elementos no array: {list.size}')

