#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLACK', 'LSTAT', 'MEDV']

for col1_idx, column1 in enumerate(df.columns):
   for col2_idx, column2 in enumerate(df.columns):
      if col1_idx < col2_idx:
         fig, axes = plt.subplots(1, 1, figsize=(8,8))
         axes.scatter(df[column1], df[column2], label=f'{column1} to {column2}', color='green', marker='x')
         axes.set_title(f'{column1} to {column2}')
         axes.set_xlabel(column1)
         axes.set_ylabel(column2)
         axes.legend()
         plt.show()
         plt.clf()
         plt.close()
