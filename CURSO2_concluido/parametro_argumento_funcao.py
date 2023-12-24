
# Functions (Funções)
    # DRY - Don't repeat yourself (Não se repita).
    # Paramentro --> Argumento

def boas_vindas(nome, quantidade):
    print(f"Olá {nome}.")
    print(f"Temos {str(quantidade)} notebooks em estoque")

boas_vindas("Marcos", 5)
boas_vindas("Ronaldo", 4)
boas_vindas("Linda", 2)


'''
def boas_vindas_Marcos():
    print("olá Marcos!")
    print("Temos 5 notebooks em estoque")

def boas_vindas_Ronaldo():
    print("olá Ronaldo!")
    print("Temos 4 notebooks em estoque")

def boas_vindas_Linda():
    print("olá Linda!")
    print("Temos 2 notebooks em estoque")

boas_vindas_Marcos()
boas_vindas_Ronaldo()
boas_vindas_Linda()
'''