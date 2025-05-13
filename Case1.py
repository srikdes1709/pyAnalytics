#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 12 19:45:09 2025

@author: srikardesikan
"""
#import data into python
url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(url)
df
df.shape
df.columns
df.head(n=3)
len(df)
df.describe()
df.dtypes

pd.set_option('display.max_columns', 15)
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
df.describe()

df['region'] = df['region'].astype('category')
df.describe()

df.region.value_counts()
df.region.value_counts().plot(kind='bar')

#Who are the most loyal customers
df.custname.value_counts().sort_values(ascending = False).head(5)
df.groupby('custname').size().sort_values(ascending = False).head(5)

#Customers who contribute the most to the revenue
df.groupby('custname').revenue.sum().sort_values(ascending = False).head(5)
df.groupby('custname').aggregate({'revenue':[np.sum,max,min]})

#Most sold items
df.groupby('partnum').size().sort_values(ascending = False).head(5)

#Part Number that brings in most revenue and margin
df.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum', ascending = False).head(5)
df.groupby('partnum')['revenue'].aggregate([np.sum]).sort_values(by='sum', ascending = False).tail(5)

#Regions that contribute maximum revenue with plot
df[['revenue', 'region']].groupby('region').sum().sort_values(by = 'revenue', ascending = False).plot(kind='bar')
