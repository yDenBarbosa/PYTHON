import numpy as np

# arr = np.array(1,2,3,4)
# arr = np.array("apple", "banana", "cherry")
# arr = np.array([1,2,3,4], dtype = "S")
# arr = np.array([1,2,3,4], dtype = "i")
# arr = np.array([1.1,2.2,3.3,4.4])
# newarr = arr.astype('i')
# arr = np.array([1,0,3,4])
# newarr = arr.astype(bool)
# arr = np.array([1,2,3,4,5])
# newarr = arr.copy()
# x = arr.copy()
# arr[0] = 42

# print(x)
# print(arr)

# arr = np.array([1,2,3,4,5])
# x = arr.view()

# arr[1] = 42

# print(x)
# print(arr)

# arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arr.shape)
# print(arr)

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(4,3)
# print(newarr)

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(2,3,2)
# print(newarr)

# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(2,4).base)

# arr = np.array([[1,2,3],[4,5,6]])
# newarr = arr.reshape(-1)
# print(newarr)

# arr = np.array([1,2,3])
# arr = np.array([
#     [1,2,3],[4,5,6]])
# for x in arr:
#     print(x)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr3 = np.array([7,8,9])
# arr = np.concatenate((arr1, arr2, arr3))
# print(arr)

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])

# arr = np.concatenate((arr1, arr2))
# print(arr)

# arr1 = np.array([[1,2],[3,4]])
# arr2 = np.array([[5,6],[7,8]])

# arr = np.concatenate((arr1, arr2), axis=1)
# print(arr)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.hstack((arr1, arr2))
# print(arr)

# arr1 = np.array([1,2,3,4,5,6])
# arr = np.array_split(arr1, 3)
# print(arr)

# arr1 = np.array([1,2,3,4,5,6])
# arr = np.array_split(arr1, 3)
# print(arr[0])
# print(arr[1])
# print(arr[2])

# arr1 = np.array([1,2,3,4,5,4,4])
# x = np.where(arr1 == 4)
# print(x)

# arr1 = np.array([1,2,3,4,5,4,4])
# x = np.where(arr1 != 4)
# print(x)

# arr1 = np.array([1,2,3,4,5,4,4])
# x = np.where(arr1 > 4)
# print(x)

# arr = np.array([3,2,4,0,1,5])
# print(np.sort(arr))

# arr = np.array(['tata', 'eva', 'joao', 'maria'])
# print(np.sort(arr))

# arr = np.array(['tata', 'eva', 'joao', 'maria'])
# arr1= np.array([True, False, False, True, True])
# print(np.sort(arr))
# print(np.sort(arr1))

# arr = np.array(['tata', 'eva', 'joao', 'maria', 'telma'])
# x = arr[[True, False, False, True, True]]
# print(x)

# arr = np.array([22,34,28,10,45])
# x = arr[[True, False, False, True, True]]
# print(x)

# arr = np.array([22,34,28,10,45])
# filtro_arr = []
# for element in arr:
#     if element > 30:
#         filtro_arr.append(True)
#     else:
#         filtro_arr.append(False)

# newarr = arr[filtro_arr] 
# print(filtro_arr)
# print(newarr)

arr = np.array([22,34,28,10,45])
filtro_arr = []
for element in arr:
    if element % 2 == 0:
        filtro_arr.append(True)
    else:
        filtro_arr.append(False)

newarr = arr[filtro_arr] 
print(filtro_arr)
print(newarr)
