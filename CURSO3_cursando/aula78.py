# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def mult(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


numeros = (3, 3, 3, 10)
resultado = mult(*numeros)
print(resultado)


# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o númerp é par ou ímpar.

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(9))
print(par_impar(7))
print(par_impar(20))
