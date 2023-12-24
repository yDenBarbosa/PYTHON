
x = float(input("Digite a primeira nota: "))
y = float(input("Digite a segunda nota: "))

notaFinal = x + y

if notaFinal > 60:
    print(f"NOTA FINAL = {notaFinal:.1f}")
else:
    print(f"NOTA FINAL = {notaFinal:.1f}")
    print("REPROVADO")
