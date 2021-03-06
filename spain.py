# -*- coding: utf-8 -*-
"""Spain.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/190PgJVyZ4w8DZ7GwckuHG7Mm3b_CCI9n
"""

#imports
import pandas as pd
import seaborn as sns

#Import data from source
from google.colab import files
uploaded = files.upload()

data = pd.read_csv('datos_provincias.csv')

data.head()

df1 = data['fecha'].str.contains("2020-04-15") 
today = data[df1]

dates = data['fecha'].unique()
dates

total = today[['provincia_iso']]
for date in dates:
  day = data[ data['fecha'].str.contains(date) ]
  reports = list(day['num_casos'])
  total[date] = reports

total.head()

sns.heatmap(total)

#saving to drive
from google.colab import drive
drive.mount('/drive')

total.to_csv('/drive/My Drive/Colab Notebooks/Spain.csv')

