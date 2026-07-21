import pandas as pd
import numpy as np
data={'name':['Amit','Riya','Kabir ','Neha','Suresh','Priya'],
      'age':[25,30,22,np.nan,28,35],
      'city':['Delhi','Mumbai','pune','Delhi','Chennai','Mumbai'],
      'salary':[40000,55000,30000,45000,60000,np.nan],
      'department':['Sales','IT','Sales','HR','IT','HR'],
      }
df=pd.DataFrame(data)
print(df)
#q1
print("question 1")
salary_series=pd.Series([40000,55000,30000,45000,60000,np.nan])
print(salary_series.dtype)
print(salary_series.size)
print(salary_series.index)

#q2
print("question 2")
print(df.info())
print(df.describe())
print(df.shape)
print(df.dtypes)
#q3
print("question 3")
print(df['city'])
print(df.iloc[1])
print(df.loc[df['name']=='Riya'])
print(df.at[3,'salary'])
#q4
print("question 4")
print(df.sort_values('salary',ascending=False))
print(df.sort_index)
print(df.drop('department',axis=1))
print(df.rename(columns={'salary':'income'}))
df['age']=df['age'].fillna(df['age'].mean()).astype(int)
#q5
print("question 5")
print(df[df['city']=='Mumbai'])
print(df['city'].isin(['Delhi','Pune']))
print(df[df['age'].between(25,30)])
#q6
print("question 6")
print(df.isna())
print(df.dropna())
print(df['age'].fillna(df['age'].mean()))
print(df['salary'].interpolate())
#q7
print("question 7")
print(df.groupby('department')['name'].count())
print(df.groupby('department')['salary'].mean())
print(df.groupby('department')['age'].agg(['min','max']))
#q8
print("question 8")
df['Bonus']=df['salary'].apply(lambda x:x*0.10)
df['city_shot']=df['city'].map(lambda x:x[:3])
df['position']=df['age'].apply(lambda x: 'senior' if x>28 else 'junior')
#q9
print("question 9")
df.to_csv("practice.csv",index=False)
df2=read_csv("practice.csv")
print(df.to_dict())




#dont know
series
dtype
loc
iloc
at
sort_index
isin
query
interpolate
map

      


