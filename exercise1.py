#!/usr/bin/env python3

import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/boston/housing.data',
                 sep='\s+',
                 header=None)

df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLACK', 'LSTAT', 'MEDV']

plt.plot(df['BLACK'])
plt.title('BLACK')
plt.xlabel('BLACK')
plt.ylabel('Count')

plt.show()
plt.clf()
plt.close()

plt.scatter(df['BLACK'], df['TAX'])
plt.title('BLACK to TAX')
plt.xlabel('BLACK')
plt.ylabel('TAX')

plt.show()
plt.clf()
plt.close()

