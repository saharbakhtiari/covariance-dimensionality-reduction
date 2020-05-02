import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.style import library

data = pd.read_csv('Train_UWu5bXk.csv')
# print(data.isnull().sum())

data['Item_Weight'].fillna(data['Item_Weight'].median(),inplace=True)
data['Outlet_Size'].fillna(data['Outlet_Size'].mode()[0],inplace=True)

corr=data.corr()
corr_col=np.array(corr.columns)
col_data=[]
for i in range(0,len(corr)):
    for j in range(i+1,len(corr)):
        if((corr.iloc[i,j]>0.5 and corr.iloc[i,j]<1)or(corr.iloc[i,j]<0 and corr.iloc[i,j]<-0.5) ):
            col_data.append(corr_col[i])
for i in range(0,len(col_data)):
    data.drop(columns=col_data[i],inplace=True)
print("*********************************")

print('Removed Cols Name:')
print(col_data)