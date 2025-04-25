# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionario com outro

pessoa = {
    'nome': 'Denis',
    'sobrenome': 'Whinchester',
    'idade': 18
}


pessoa.setdefault('idade', 22)
print(pessoa['idade'])
# print(len(pessoa))

# print(list(pessoa.keys()))
# for chave in pessoa:
#     print(chave)
    
    
# print(list(pessoa.values()))
# for valor in pessoa.values():
#     print(valor)
    
    
print(list(pessoa.items()))
for chave, valor in pessoa.items():
    print(chave, valor)