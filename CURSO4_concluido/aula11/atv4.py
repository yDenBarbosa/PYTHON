import pandas as pd

df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')

# for x in df.index:
#     if df.loc[x, "Duration"] > 120:
#         df.loc[x, "Duration"] = 120
# print(df.to_string())

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace= True)
print(df.to_string()) #vai deletar a linha 7 por conta do seu valor que era 450