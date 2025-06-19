salario = float(input('Digite seu salario: '))
aumento = int(input('Digite o aumento em %: '))
ajuste = salario * (aumento/100) + salario
print(f'Seu salario ajustado é: {ajuste:.2f}')