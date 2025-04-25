# Manipulação de chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Denis Barbosa'
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])

pessoa[chave] = 'Vitória'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

#print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])