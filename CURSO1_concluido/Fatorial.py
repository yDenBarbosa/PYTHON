N = int(input("Digite n: "))

prod = N
cont = N-1

while cont > 1:
    prod = prod * cont
    cont = cont - 1
    
print(N, " ! = ", prod)