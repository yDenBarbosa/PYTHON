import math

base = float(input("Base do retangulo: "))
altura = float(input("Base do retangulo: "))

area = base * altura
perimetro = (base+altura) * 2
diagonal = math.sqrt(pow(base, 2.0) + pow(altura, 2.0))

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
