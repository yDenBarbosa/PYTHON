import pandas as pd

# data = {'calories': [420,380,390], 'duration': [50,40,45]}
# df = pd.DataFrame(data)
# # print(df)
# # print(df.loc[1])
# print(df.loc[[0,2]])

# data = {'calories': [420,380,390], 'duration': [50,40,45]}
# df = pd.DataFrame(data)
# print(df.loc[[0,1,2]])

data = {'calories': [420,380,390,270], 'duration': [50,40,45,43]}
df = pd.DataFrame(data, index=['day1', 'day2', 'day3', 'day4'])
print(df.loc['day3'])