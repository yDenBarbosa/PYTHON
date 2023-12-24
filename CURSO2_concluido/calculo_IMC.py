# Calculo de IMC - Indice de Massa Corporal

'''

Qual é a sua Altura em cm:
Qual é o seu peso em kg:

# MENOR QUE 18,5 MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0 OBESIDADE GRAVE
'''

altura = float(input("Qual é a sua Altura em cm: "))
peso = float(input("Qual é o seu peso em kg: "))

IMC = peso / (altura/100)**2

if IMC <= 18.5:
    print(f"{IMC:.1f} Magreza")
elif IMC >= 18.6 and IMC < 24.9:
    print(f"{IMC:.1f} Normal")
elif IMC >= 25.0 and IMC < 29.9:
    print(f"{IMC:.1f} Sobrepeso ")
elif IMC >= 30.0 and IMC < 39.9:
    print(f"{IMC:.1f} Obesidade")
else:
    print(f"{IMC:.1f} Obesidade Grave")


