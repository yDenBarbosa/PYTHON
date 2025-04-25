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

p1 = {
    'nome': 'Denis',
    'sobrenome': 'Whinchester',
}

# get - obtém uma chave
print(p1['nome'])
print(p1.get('nome', 'Não existe'))

# pop - apaga um item com a chave especificada (del)
nome = p1.pop('nome')
print(nome)
print(p1)

# popitem - apaga o último item adicionado
ultima_chave = p1.popitem()
print(ultima_chave)
print(p1)

# update - atualiza um dicionario com outro
p1.update({
    'nome': 'nove valor',
    'idade': 30,
})
print(p1)

# update - atualiza um dicionario com outro (com argumentos nomeados)
p1.update(nome='nome valor', idade=30)
print(p1)

# update - atualiza um dicionario com outro (com tupla ou lista)
tupla = (('nome', 'novo valor'), ('idade', 30))
# lista = [['nome', 'novo valor'], ['idade', 30]]
p1.update(tupla)# (lista)
print(p1)
