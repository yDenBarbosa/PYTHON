import matplotlib.pyplot as plt

# Dados para o grafico de Pizza
sistemas = ['Windows', 'macOS', 'Linux', 'Outros']
participacao = [75,15,7,3]
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'] # Cores personalizadas
explode = (0.1,0,0,0) # destava a primeira fatia('Windows')

# Criar o grafico de Pizza
plt.figure(figsize=(7,7)) # Grafico de Pizza ficam melhores em figuras quadradas
plt.pie(participacao, explode=explode, labels=sistemas, colors=cores, autopct='%1.1f%%', shadow=True, startangle=90)
# autopct: formata a porcentagem exibida na fatia
# shadow: adiciona uma sombra
# startagle: inicia a primeira fatia no angulo especificado(90 graus = topo)
# explode: uma tupla qie define o quanto cada fatia é 'destacada' do centro 0.1 para a primeira fatia(Windows) e 0 para outras
# plt.pie: cria o grafico de pizza
# labels = sistemas: define os rotulos para cada fatia

# Adiciona Titulo
plt.title('Participação de Mercado de Sistemas Operacionais(Desktop)\n')

# Garante que o circulo seja desenhado como um circulo
plt.axis('equal')

# Exibir o grafico
plt.show()