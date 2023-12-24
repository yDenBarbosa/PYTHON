# Desafio com If, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues.
O usuário deverá fornecer a temperatura.

Temperaturas — Cozimento
120°F ou 48°C — Rare (Selada)
130°F ou 54°C — Medium rare (Ao ponto para o mal)
140°F ou 60°C — Medium (Ao ponto)
150°F ou 65°C — Medium well (Ao ponto para o bem)
160°F ou 71°C — Well done (Bem passada)
'''

tem_cel = int(input("Qual é a temperatura da carne ? "))

if tem_cel < 48:
    print("RARE(SELADA)")
elif tem_cel in range(49, 54):
    print("MEDIUM RARE(AO PONTO PARA O MAL)")
elif tem_cel in range(55, 60):
    print("MEDIUM(AO PONTO)")
elif tem_cel in range(61, 65):
    print("MEDIUM WELL(AO PONTO PARA O BEM)")
elif tem_cel in range(66, 71):
    print("WELL DONE(BEM PASSADA)")
elif tem_cel >= 72:
    print("BURNED(QUEIMADA)")


