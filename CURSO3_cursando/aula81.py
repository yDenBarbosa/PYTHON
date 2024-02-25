# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quaduplicar(numero):
#     return numero * 4

# print(duplicar(5))
# print(triplicar(5))
# print(quaduplicar(5))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(9))
print(quadruplicar(7))


def criar_divisor(divisor):
    def dividir(numero):
        return numero / divisor
    return dividir

metade = criar_divisor(2)
um_quarto = criar_divisor(4)
um_decimo = criar_divisor(10)

print(int(metade(30)))
print(um_quarto(30))
print(um_decimo(30))

def criar_somador(somador):
    def somar(numero):
        return numero + somador
    return somar

somar_um = criar_somador(1)
somar_dez = criar_somador(10)

print(somar_um(56))
print(somar_dez(3))
