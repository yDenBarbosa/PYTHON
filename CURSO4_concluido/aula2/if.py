media = float(input('Informe a media: '))
if media > 5:
    print('Aprovado')
elif media >= 4: #and media <= 4.99:
    print('Recuperação')
else:
    print('Reprovado')