import pandas as pd

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
# # print(df)
# new_df = df.dropna()
# print(new_df.to_string())

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
# df.dropna(inplace=True)
# print(df.to_string())

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
# df.fillna(130,inplace=True)
# print(df.to_string())

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
# df.fillna({"Calories":140},inplace=True) #substitue os vazios por 140
# print(df.to_string())

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
# x = df["Calories"].mean()
# df.fillna({"Calories":x},inplace=True) #substitue os vazios por 140
# print(df.to_string())

df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
x = df["Calories"].mode()[0]
df.fillna({"Calories":x},inplace=True) #substitue os vazios por 140
print(df.to_string())