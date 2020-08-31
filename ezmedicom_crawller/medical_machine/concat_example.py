# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 08:42:28 2020

@author: User
"""

import pandas as pd 
import numpy as np 


import matplotlib.pyplot as plt 



def analysisCorelationship(df):
    
    df = df.corr().dropna(how = 'all').dropna(axis = 1 , how = 'all')
    
    df = df.where(np.triu(np.ones(df.shape)).astype(np.bool))
    
    
    lst = list(df.columns)
    
    for i in lst:
        
        
      
        if (df[df[i] <= 0.25].empty) == False :
            lst2 = list(df[df[i] < 0.25].index)
            
            for j in lst2:
                
            
                print(i," 는 ",j," 와 연관성이",df.loc[j,i], "의 수치로 상당히 낮습니다.")
                
        if ( df[(df[i] > 0.25) & (df[i] <= 0.5) ].empty) == False :
            lst2 = list(df[df[i] < 0.5].index)
            for j in lst2:
                
            
                print(df.i," 는 ",j," 와 연관성이",df.loc[j,i], "의 수치로 낮습니다.")
        if (df[(df[i] > 0.5) & (df[i] <= 0.75)].empty) == False :
            lst2 = list(df[df[i] < 0.75].index)
            
            for j in lst2:
                
            
                print(df.i," 는 ",j," 와 연관성이",df.loc[j,i], "의 수치로 높습니다.")
        
        if (df[(df[i] > 0.75) & (df[i] < 1)].empty) == False :
            lst2 = list(df[df[i] < 1].index)
            for j in lst2:
                
            
                print(df[i]," 는 ",j," 와 연관성이",df.loc[j,i], "의 수치로 상당히 높습니다.")



def find_outlier(df,column):
    df1 = df.copy()
    df1['label'] = 0 
    
   
    
    data = df1[column]
    
    q25 = np.percentile(data,25)
    q75 = np.percentile(data,75)
    
    r = q75-q25
    r = r * 1.5
    lowest = q25 - r
    highst = q75 + r 
    outlier = list(data[  (data<lowest) | (data > highst) ])
    
    
    df1['label'] = df1.apply(lambda x  :  1 if (x[column] in outlier) else 0 , axis = 1 )
    
    
    
    return df1
    


def show(df,column):
    
    
    plt.title("이상치분석")
    
    plt.scatter(x = df[column], y = [0]*df.shape[0],alpha = 0.2,s = 300, c = df['label'])

    plt.show()
if __name__ == "__main__":
    

    a = pd.read_excel('C:/Users/User/Downloads/예시.xls',encoding='utf-8')



    
    edi = list(a['EDI CODE'].drop_duplicates())
    
    
    test1 = a[a['EDI CODE'] == edi[0]][['EDI CODE','보험가','계약단가(가)']]
    
    analysisCorelationship(a)
    
    test1 = find_outlier(test1, '계약단가(가)')
    
    print(test1)
    
    show(test1,'계약단가(가)')
    print('이상치 x')
    print(test1[test1['label']==0])
    print("-----------------\n\n\n")
    print('이상치\n')
    print(test1[test1['label']==1])
    
    