
x = int(input("Digite a quantidade de minutos: "))

pagar = 50

if x > 100:
    pagar = 50.00 + 2 * (x - 100)


print(f"Valor a pagar: R$ {pagar:.2f}")