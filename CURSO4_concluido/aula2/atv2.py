#eu
compra = float(input('Valor da compra: R$ '))
prest = int(input('Digite em quantas parcelas será feito o pagamento: '))
juros = 2
parce = compra/prest

if prest > 4:
    parce = parce * (juros/100) + parce

print(f'A compra de R${compra:.2f} parcelada em {prest} vezes, será de R${parce:.2f}')


#professor
valort = float(input('Informe o valor total da compra: R$ '))
multa = int(input('Informe a porcentagem de multa de atraso: '))
prest = int(input('Informe o numero de prestações: '))
parcprest = valort / prest
multaporart = valort + (valort * (multa/100))
print(f'Valor a ser pago com multa é: {multaporart}')

