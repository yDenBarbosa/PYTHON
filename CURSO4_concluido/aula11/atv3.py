import pandas as pd

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# print(df.to_string())

# df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# df.dropna(subset=['Date'], inplace=True)
# print(df.to_string())

df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula11/data2.CSV')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace=True)
df.loc[7,'Duration'] = 45 #corrigiu o dado do campo DURATION, na linha sete para "45"
print(df.to_string())