import matplotlib.pyplot as plt
import numpy as np

#gerar dados aleatorios 
np.random.seed(42) #parar reprodutibilidade
x=np.random.rand(50)
y=np.random.rand(50)
cores = np.random.rand(50) #cores aleatorias para os pontos
tamanho = 100 * np.random.rand(50) #tamanhos aleatorios para os pontos

#criar grafico
plt.figure(figsize=(7,5))
plt.scatter(x, y, c=cores, s=tamanho, alpha=0.6, cmap='viridis')#c=cores, s=tamanho, cmap são opcionais

#adicionar titulo
plt.title('Grafico de dispersão aleatorio')
plt.xlabel('Eixo x Aleatorio')
plt.ylabel('Eixo y Aleatorio')

#adicionar uma barra de cores (se estiver usando cmap)
plt.colorbar(label='Intensidade da Cor') #descomente se quiser mostrar a barra de cores

#exportar o grafico
plt.savefig('dispersao_aleatoria.png') #salva como PNG
plt.savefig('dispersao_aleatoria.pdf') #salva como PDF  

print('Gráficos exportados como "dispersao_aleatoria.png" e "dispersao_aleatoria.pdf"')

#exibir o grafico (opcional, pois ja foi salvo)
plt.show()
