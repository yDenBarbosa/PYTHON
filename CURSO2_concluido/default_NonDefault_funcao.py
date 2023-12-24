
# Functions (Funções)
    # DRY - Don't repeat yourself (Não se repita).
    # Paramentro --> Argumento
    # Default = Aquele que você define o valor no parametro(SEMPRE POR ULTIMO)
    # Non-Default = Aquele que você não define o valor no parametro

def boas_vindas(quantidade, nome="Linda"):
    print(f"Olá {nome}.")
    print(f"Temos {str(quantidade)} notebooks em estoque")

boas_vindas(6)