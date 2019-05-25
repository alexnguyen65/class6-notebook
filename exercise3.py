#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLACK', 'LSTAT', 'MEDV']

fig, axes = plt.subplots(2, 1, figsize=(8,8))

axes[0].plot(df['BLACK'])

axes[0].plot(df['BLACK'])
axes[0].set_title('BLACK')
axes[0].set_xlabel('BLACK')
axes[0].set_ylabel('Count')

axes[1].scatter(df['BLACK'], df['TAX'])

axes[1].scatter(df['BLACK'], df['TAX'])
axes[1].set_title('BLACK to TAX')
axes[1].set_xlabel('BLACK')
axes[1].set_ylabel('TAX')

plt.tight_layout()
plt.show()
plt.clf()
plt.close()

