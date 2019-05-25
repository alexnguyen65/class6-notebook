#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLACK', 'LSTAT', 'MEDV']

fig, axes = plt.subplots(1, 1, figsize=(8,8))

axes.scatter(df['BLACK'], df['TAX'], color='red', marker='v', alpha=0.8, s=df['CRIM'])

axes.scatter(df['BLACK'], df['TAX'])
axes.set_title('BLACK to TAX')
axes.set_xlabel('BLACK')
axes.set_ylabel('TAX')

plt.tight_layout()
plt.show()
plt.clf()
plt.close()

