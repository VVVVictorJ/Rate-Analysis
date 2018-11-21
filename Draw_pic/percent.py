import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

data=pd.read_excel(r'C:\Users\Pasto\Desktop\etar.xlsx',sheet_name='Sheet3')
data.rename(columns={'赛事':'A','独赢':'B','全场 - 让球':'C','全场 - 大小':'D','单双':'E','胜负':'F'},inplace=True)
data=data[['A','B','C','D','E','F']]
all=data['F'][data.F>=-1].value_counts()
print(all[1])
#data=data[['A','B','F']][data.F==1]
#data=data[['B','F']][(data.F==1)&(data.B>1)&(data.B<1.24)]
count=data['B'][(data.F==1)&(data.B>1)&(data.B<1.24)].value_counts()
count2=data['B'][(data.F==1)&(data.B>0)&(data.B<1)].value_counts()
print(len(count2))
if len(count2)==0:
    print(666)
#count=data['F'].value_counts()
#count=data['F'][data.F==1].value_counts()
# print(count)
print(count2)
#print('precent: {:.2f}%'.format(count[1]/all[1]))
#print(data)

# count3=data['F'][(data.F==1)&(data.B>i)&(data.B<j)].value_counts()
# i=j
# j=j+0.04
# count4=data['F'][(data.F==1)&(data.B>i)&(data.B<j)].value_counts()
# print(count3[1])
# print(count4[1])
i=1
j=1.24
print("kaishi")
for z in range(200):
    print('precent1: {:.1f}'.format(i),'precent2: {:.1f}'.format(j))
    count5=data['F'][(data.F==1)&(data.B>i)&(data.B<j)].value_counts()
    if len(count5)==0:
        i=j
        j=j+0.04
        continue
    print(count5[1])
    i=j
    j=j+0.04




