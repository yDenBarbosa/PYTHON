import pandas as pd

df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
df.drop_duplicates(inplace=True)
print(df.to_string()) #remove os duplicados