# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:42:45 2021

@author: Chetan
"""
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import re
data = pd.read_csv("D:\\widya\\instagram_reach.csv")
data.info()
data.columns
data = data.drop(['Unnamed: 0', 'S.No', 'USERNAME', 'Caption', 'Hashtags'],axis=1)
data.columns
data["Time since posted"] = data["Time since posted"].apply(lambda x : x.replace("hours", ""))
data["Time since posted"]=data["Time since posted"].astype(int)
data.info()

X= data[["Followers","Time since posted"]]
y = data["Likes"]
model = LinearRegression()
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)
pred = model.predict(X_test)

from sklearn.metrics import mean_squared_error

mean_squared_error(y_test,pred)
