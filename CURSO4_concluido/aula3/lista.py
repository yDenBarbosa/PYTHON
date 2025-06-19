# a = [3, 'john', 5.0, 7]
# x = (a[1])
# print(x)

# a = [[3,'john',5.0,7],[4,6,8]]
# x = (a[1][2])
# print(x)

# a = [[3,'john',5.0,7],[-1,4,6,-8],[3,6,5,9]]
# x = (a[2][2])
# print(x)

# a = [[3,'john',5.0,7],[-1,4,6,-8],[3,6,5,9]]
# print(a[1]) #a lista dentro da lista no indicie 1
# print(a) #todas as listas

# lista=[]
# x=int(input('Digite a sua idade: '))
# lista.append(x) #insere a idade recebida do input na lista
# print(lista)

# lista=[3,6,1]
# x=int(input('Digite a sua idade: '))
# lista.insert(1, x) #insere a idade recebida do input na lista no indicie "1"
# print(lista)

# lista=[3,6,1]
# x=int(input('Indique o numero para remover : '))
# lista.remove(x) #remove o numero indicado pelo input
# print(lista)

lista=[[3,6,1],[1,2,3]]
x=int(input('Indique o numero para remover : '))
del lista[1] #remove a lista localizada no indicie "1"
print(lista)