import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import math as mt
from scipy.stats import mode

df = pd.read_csv('C:/Users/senai/Desktop/Denis/aula12/iris.csv')
df.head()

# print(df.head(10))
# print(df.describe())

dfc = df.drop(columns = 'Id') #Drops the obsolete ID column
xvars = dfc.select_dtypes(include = 'number') #Selects only numerical variables
cor_matrix = xvars.corr()
# print(cor_matrix)

config, axis = plt.subplots(nrows = 2, ncols = 2, figsize = (14,14))
comparison = 'PetalLengthCm'

sns.set(style = 'whitegrid')
for ax, x_value in zip(axis.flat, xvars):
    sns.scatterplot(data = df, x = x_value, y = comparison, hue = 'Species', ax=ax, palette = ['Blue', 'Navy', 'Purple'])

# plt.show()

if 'Id' in df.columns:
    df = df.drop(columns = 'Id') #Id is obsolete

def remove_outliers(df):

    origin_length = len(df)
    
    for col in df.select_dtypes(include = 'number').columns:
        
        upper = np.percentile(df[col], 75)
        lower = np.percentile(df[col], 25)
    
        IQR = upper - lower
    
        threshold_low = lower - IQR * 1.5
        threshold_high = upper + IQR * 1.5
    
        df = df[(df[col] >= threshold_low) & (df[col] <= threshold_high)]


    removed = origin_length - len(df)
    print(f'{removed} outliers have been removed.')
    
    return df

df = remove_outliers(df)
na_df = df.dropna()
print('DataFrame has',len(na_df), 'entries.')
print('Removed', len(df) - len(na_df), 'missing values.')

