"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

# def soma(x, y):
#     #Definição
#     print(f'{x=} y={y}', '|', 'x + y = ', x + y)
    
    
# soma(1, 2)

def soma(x, y, z):
    #Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)
    
    
soma(1, 2, 3)
soma(y=2, x=1, z=3)
#soma(2, x=1, 3) erro 