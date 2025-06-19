import pandas as pd
import numpy as np


data = pd.read_json('C:/Users/senai/Desktop/Denis/aula11/data0.json')
df = pd.DataFrame(data)
# print(df)
# print(df.head(3)) #mostra 3 primeiras linhas
# print(df.tail(3)) #mostra 3 ultimas linhas
print(df.info()) #mostra informações dos dados