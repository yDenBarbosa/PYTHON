#eu
idade = int(input('Digite a idade do nadador: '))

if idade < 5:
    print('Sem classificação')
elif idade <= 7:
    print('Infantil A')
elif idade <= 11:
    print('Infantil B')
elif idade <= 13:
    print('Juvenil A')
elif idade <= 17:
    print('Juvenil B')
else:
    print('Adultos')


#professor
idade = int(input('Informe a idade: '))
if idade < 5:
    print('Sem classificação')
elif idade >= 5 and idade <= 7:
    print('Pertence a Categoria Infantil A')
elif idade >= 8 and idade <= 11:
    print('Pertence a Categoria Infantil B')
elif idade >= 12 and idade <= 13:
    print('Pertence a Categoria Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Pertence a Categoria Juvenil B')
else:
    print('Pertence a Categoria Adultos')