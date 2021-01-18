# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:42:43 2021

@author: Chetan
"""
import pandas as pd 
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
data  = pd.read_csv("covid19.csv")

data.info()
data.head()
df = pd.DataFrame(data.groupby("Date",sort=False).sum()).reset_index()
print(df.columns)
df["total"]=(df["ConfirmedIndianNational"]+df["ConfirmedForeignNational"])+(df["Cured"]+df["Deaths"]) 
df1 = df[df.index>33]

rate = []
for i in range(34,51):
    rate.append((df1["total"][i+1]-df1["total"][i])/df1["total"][i])

rate.append(0)
df1["rate"].mean()
rate.mean()
31*np.exp(0.14*26)