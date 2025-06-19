from numpy import random
import numpy as np

# x = random.randint(100)
# x = random.randint(100, size=(4)) matriz
# x = random.randint(100, size=(4,4)) #matriz 4x4


# x = random.choice([3,5,7,9]) #apresenta um numero da lista
# x = random.choice([3,5,7,9], size=(3,3)) #matriz 3x3
# x = random.choice([3,5,7,9], p=[0.4,0.3,0.3,0.0], size=(10)) #p=probabilidade do numero no indicie ser escolhido
# x = random.choice([3,5,7,9], p=[0.0,0.9,0.0,0.1], size=(3,5)) #p=probabilidade do numero no indicie ser escolhido matriz 5x3

# arr = np.array((1,2,3,4,5)) #tupla, sem alterações
arr = np.array([1,2,3,4,5])
print(arr)
print(random.permutation(arr))