'''
 Exercício 3: Indexação e Fatiamento (Slicing)

Crie um array NumPy 2D (matriz) com 3 linhas e 4 colunas contendo números de 1 a
12. (Dica: use np.arange() e reshape()).

Em seguida:

a) Imprima a matriz completa.
b) Imprima o elemento na segunda linha e terceira coluna.
c) Imprima a primeira linha inteira.
d) Imprima a última coluna inteira.
e) Imprima um subarray contendo os elementos das duas primeiras linhas e das duas
últimas colunas.'''


import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(3,4)
# print(f'Matriz completa {newarr}')

matriz = np.arange(1,13).reshape(3,4)
elemento = matriz[1,2]
first_line = matriz[0, :] #ou matriz[0]
last_line = matriz[:,3]
subarray = matriz[0:2, 2:4]

print(f'Matriz completa:\n{matriz}\n')
print(f'Elemento na segunda linha, terceira linha: {elemento}\n')
print(f'Primeira linha inteira: {first_line}')
print(f'Ultima coluna inteira:\n{last_line}\n')
print(f'Subarray (2 primeiras linhas e 2 ultimas colunas):\n{subarray}')