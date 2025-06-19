import matplotlib.pyplot as plt
import numpy as np

# Gerar dados aleatorios com distribuição norma
np.random.seed(101)
media = 70
desvio_padrao = 10
n_amostras = 1000
notas = np.random.normal(media, desvio_padrao, n_amostras) # Gera numeros aleatorios de uma distribuição normal

# Criar histograma
plt.figure(figsize=(8,6))
plt.hist(notas, bins=15, color='skyblue', edgecolor='black', alpha=0.9) # Cria histograma, bins defino o numero fe intervalos
# edgecolor adiciona uma borda as barras para melhorar a distinção
 
# Adicionar titulo e rotulos
plt.title('Distribuição de notas dos alunos')
plt.xlabel('Notas')
plt.ylabel('Frequencia')

# Adicionar uma linha vertical para media (opcional)
plt.axvline(notas.mean(), color='red', linestyle='dashed', linewidth=1, label= f'Media: Média: {notas.mean():.2f}')
plt.legend()
# plt.axvline adiciona uma linha no grafico, util para ,arcar pomtos de referencia como media

# Adicionar grade
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exibir o grafico
plt.show()