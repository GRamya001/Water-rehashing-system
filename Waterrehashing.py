# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:54:34 2019

@author: Ramiya
"""
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
df = pd.read_csv('F:\Hack SRM\idata.csv')
x=df['quantity']
y1=df['zn']
df = pd.DataFrame(x)
#df.columns = df.feature_names
train_x, test_x, train_y1, test_y1 = model_selection.train_test_split(x, y1)
train_x = train_x.reshape(-1,1)
test_x = test_x.reshape(-1,1)
alg = LinearRegression()
alg.fit(train_x,train_y1)
y1_pred = alg.predict(test_x)
x_inp=int(input("Enter Quantity water: "))
y1_out=alg.predict(x_inp)
plt.scatter(y1_pred,test_x)
plt.show()
print('R2 Score:',r2_score(test_y1,y1_pred))
if(y1_out>=4.5):
    print("Try with ION EXCHANGE METHOD")
else:
    print("Quantity of water in zinc is normal")




