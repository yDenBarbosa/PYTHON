import pandas as pd

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula10/data.csv')
# ds = df #copia para fazer alterações OBS: nunca mexer na original
# # print(ds) #imprime só os 5 primeiros e os ultimos
# # print(ds.to_string()) #imprime tudo
# print(pd.options.display.max_rows)

pd.options.display.max_rows = 6
df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula10/data.csv')
print(df)
