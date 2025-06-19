#eu
timeA = int(input('Digite a quantidade de gols do time A: '))
timeB = int(input('Digite a quantidade de gols do time B: '))

if timeA > timeB:
    print(f'Time A {timeA} x {timeB} Time B, vitória do time A')
elif timeA < timeB:
    print(f'Time A {timeA} x {timeB} Time B, vitória do time B')
else:
    print(f'Time A {timeA} x {timeB} Time B, empate')


#Professor
time_a = int(input('Digite a qtos gols do time A: '))
time_b = int(input('Digite a qtos gols do time B: '))

if time_a > time_b:
    print(f'Time A venceu a partida por {time_a} x {time_b}')
elif time_a < time_b:
    print(f'Time B venceu a partida por {time_a} x {time_b}')
else:
    print(f'Houve um empate Time A {time_a} x {time_b} Time B')

