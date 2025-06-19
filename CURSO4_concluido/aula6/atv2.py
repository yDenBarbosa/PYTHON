'''
Exercício 2: Operações Matemáticas Elemento a Elemento

Crie dois arrays NumPy:

arr1 com os valores [1, 2, 3, 4]
arr2 com os valores [5, 6, 7, 8]

Realize e imprima o resultado das seguintes operações elemento a elemento:

a) Adição de arr1 e arr2.
b) Subtração de arr2 por arr1.
c) Multiplicação de arr1 por arr2.
d) Divisão de arr2 por arr1.
e) arr1 elevado ao quadrado.'''


import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])

print(f'Soma dos arrays: {arr1 + arr2}')
print(f'Subtração do arr2 pelo arr1: {arr2 - arr1}')
print(f'Multiplicação do arr1 pelo arr2: {arr2 * arr1}')
print(f'Divisão do arr2 pelo arr1: {arr2 / arr1}')
print(f'Arr1 elevado ao Quadrado: {arr1 ** 2}')
