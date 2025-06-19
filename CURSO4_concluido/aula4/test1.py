import numpy as np

# print(np.__version__)

# arr = np.array([1, 2, 3, 4, 5])
# arr = np.array((1, 2, 3, 4, 5))
# arr = np.array(42) #uma dimensão
# arr = np.array([[1, 2, 3],[4, 5,6]]) #duas dimensões
# arr = np.array([[[1, 2, 3],[4, 5,6], [1,2,3],[4,5,6]]]) #quatro dimensões

# a=np.array(42)
# b=np.array([1, 2, 3, 4, 5])
# c=np.array([[1, 2, 3],[4, 5,6]])
# d=np.array([[[[1, 2, 3],[4, 5,6]], [[1,2,3],[4,5,6]]]]) #quatro dimensões
# # print(type(arr))
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# arr = np.array([1, 2, 3, 4], ndmin=10) #define a quantidade de dimensões no array ndmin=
# print(arr)
# print('Numero de dimensoes: ', arr.ndim)

# arr = np.array([1, 2, 3, 4]) 
# print(arr[0]) #mostra a informação no indicie, no caso o 0 da array

# arr = np.array([1, 2, 3, 4]) 
# print(arr[0] + arr[3]) #somando os valores dos indicies, no caso o 0 = 1 e 3 = 4 que dá 5


# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(f'Segundo elemento da primeira lista', arr[0,1])

# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(f'Segunda lista e terceiro elemento', arr[1,2])

# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(arr[1,0,2])

# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5]) #sera mostrado os valores apartir do 2 ate o 5

# arr = np.array([1,2,3,4,5,6,7])
# print(arr[4:]) #sera mostrado os valores apartir do 5 adiante

# arr = np.array([1,2,3,4,5,6,7])
# print(arr[:4]) #sera mostrado os valores apartir do 4 pra trás

# arr = np.array([1,2,3,4,5,6,7])
# print(arr[-3:-1]) 

arr = np.array([21,22,23,24,25,26,77])
print(arr[0:6:2]) 