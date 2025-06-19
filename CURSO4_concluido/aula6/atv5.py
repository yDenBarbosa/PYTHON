'''
Exercício 5: Seleção Condicional e Modificação

Crie um array NumPy usando np.arange(1, 16) (números de 1 a 15).

a) Remodele este array para uma matriz 3x5.
b) Imprima a matriz resultante.
c) Crie um novo array contendo apenas os elementos da matriz que são maiores
que 8.
d) Na matriz original, substitua todos os elementos que são múltiplos de 3 por 0.
Imprima a matriz modificada.'''


import numpy as np

arr_base = np.arange(1,16)
matriz_mod = arr_base.reshape(3,5)
mariores_oito = matriz_mod[matriz_mod > 8]
matriz_para_modificar = matriz_mod.copy()
matriz_para_modificar[matriz_para_modificar % 3 == 0] = 0

print(f'matrix 3x5:\n{matriz_mod}\n')
print(f'Elementos maiores que 8: {mariores_oito}\n')
print(f'Matriz com multiplos de 3 substituidos por 0:\n {matriz_para_modificar}')