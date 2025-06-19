import matplotlib.pyplot as plt
import numpy as np

# Dados do KPI
categorias = ['META', 'REALIZADO']
valores = [ 50000, 45000]

# Criar o gráfico de Barras
plt.figure(figsize=(6,5))
bars = plt.bar(categorias, valores, color=['skyblue', 'lightcoral'])

# Adicionar Titulos e Rótulos
plt.title('Desempenho de Vendas Mensal')
plt.ylabel('Valor (R$)')
plt.xlabel('Categorias') # Opcional, pois as categorias já estão no eixo X

# Adicionar os valore (KPIs) acima da barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 500, f'R$ {yval:,.0f}'.replace(',','.'), va='bottom', ha='center') #va: Vertical aligment, ha: Horizontal aligment

# Remover o eixo y superior e direito para um visual mais limpo(opcional)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Exibir o grafico
plt.show()