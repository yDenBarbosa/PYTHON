import matplotlib.pyplot as plt

#dados 
anos = [ '1950', '1955', '1960', '1965', '1970', '1975', '1980', '1985','1990', '1995', '2000', '2005',	'2010',	'2015',	'2020',	'2025']
populaçãoA = [52.3, 56.2, 60.3, 66.1, 73.1, 84.2, 106.0, 121.0, 146.9, 157.9, 169.5, 182.3, 190.7, 207.7, 212.6, 214.7]
populaçãoB = [370.8, 395.4, 424.1, 466.0, 548.1, 603.4, 683.3, 758.1, 846.3, 948.3, 1026.9, 1080.4, 1210.3, 1311.0, 1380.0, 1450.0]


#criar o grafico
plt.figure(figsize=(10,6)) #Define o tamanho da figura (Opcional, mas nom para visualizações)
plt.plot(anos, populaçãoA, marker='o', linestyle='-', color='r', label='População Média do Brasil') #color='primeira letra da cor em ingles'
plt.plot(anos, populaçãoB, marker='o', linestyle='-', color='b', label='População Média da Índia') #color='primeira letra da cor em ingles'

#adicionar titulo e rótulos
plt.title('POPULAÇÃO BRASILEIRA AO LONGO DOS ANOS')
plt.xlabel('LINHA DO TEMPO')
plt.ylabel('POPULAÇÃO EM MILHARES')

#adicionar legenda (caso haja mais de uma linha no futuro)
plt.legend()

#adicionar grade
plt.grid(True, linestyle='--', alpha=0.7)

#exibir o grafico
plt.show()