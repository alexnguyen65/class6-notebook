#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLACK', 'LSTAT', 'MEDV']

fig, axes = plt.subplots(1, 1, figsize=(8,8))

#axes.scatter(df['BLACK'], df['TAX'], color='red', marker='v', alpha=0.8, s=df['CRIM'])

axes.scatter(df['TAX'], df['BLACK'], color='red', s=df['CRIM'])
axes.scatter(df['TAX'], df['CRIM'], color='green', s=df['CRIM'])
axes.scatter(df['TAX'], df['INDUS'], color='blue', s=df['CRIM'])
axes.legend()

axes.set_title('My Title')
axes.set_xlabel('TAX')

plt.show()
plt.clf()
plt.close()

