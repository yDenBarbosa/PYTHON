import matplotlib.pyplot as plt

#dados 
dias = [ 'seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom']
temperaturas = [22,24,23,25,26,24,23]
temperatura = [21,24,27,25,28,24,25]

#criar o grafico
plt.figure(figsize=(8,5)) #Define o tamanho da figura (Opcional, mas nom para visualizações)
plt.plot(dias, temperaturas, marker='o', linestyle='-', color='b', label='Temperatura Média') #color='primeira letra da cor em ingles'
plt.plot(dias, temperatura, marker='o', linestyle='-', color='r', label='Temperatura Média') #color='primeira letra da cor em ingles'

#adicionar titulo e rótulos
plt.title('TEMPERATURA MEDIA SEMANAL')
plt.xlabel('DIAS DA SEMANA')
plt.ylabel('TEMPERATIRAS GRAUS ºC')

#adicionar legenda (caso haja mais de uma linha no futuro)
plt.legend()

#adicionar grade
plt.grid(True, linestyle='--', alpha=0.7)

#exibir o grafico
plt.show()