#eu
operac = int(input('Qual operação deseja: 1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - divisão: '))
entraP = float(input('Primeiro número: '))
entraS = float(input('Segundo número: '))

if operac == 1:
    print('O resultado da soma é ', (entraP + entraS))
elif operac == 2:
    print('O resultado da soma é ', (entraP - entraS))
elif operac == 3:
    print('O resultado da soma é ', (entraP * entraS))
elif operac == 4:
    print('O resultado da soma é ', (entraP / entraS))
else:
    print('Opção invalida')
    
    
#professor
num1 = float(input('Informe um número: '))
num2 = float(input('Infotme um número: '))
x = int(input('seleciona a Operação desejada:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - divisão: '))

if x == 1:
    soma = num1 + num2
    print(f'O resultado da Soma é : {soma}')
elif x == 2:
    sub = num1 - num2
    print(f'O resultado da Subtração é : {sub}')
elif x == 3:
    mult = num1 * num2
    print(f'O resultado da Multiplicação é : {mult}')
elif x == 4:
    div = num1 / num2
    print(f'O resultado da Divisão é : {div}')
else:
    print('Escolheu Errado !!!')
    