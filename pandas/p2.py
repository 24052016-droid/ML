import pandas as pd
data={"name":["a","b","c"],"age":[20,30,40],"score":[1,2,3]}
df=pd.DataFrame(data)
print(df.iloc[0:2])
print(df[df['age']>30])
print(df.isnull())
print(df.dropna())
df.rename(columns={"name":"full name"},inplace=True)
df.replace("a","angel",inplace=True)
df.replace("b","bina",inplace=True)
df.replace("c","cherry",inplace=True)
print("mean is ",df['age'].mean())
print("sum is ",df['age'].sum())
print("min is",df['age'].min())
print("max is ",df['age'].max())
print("mode is ",df['age'].mode())
print("median is ",df['age'].median())
print(df.sort_values(by="age",ascending=False))#default is ascending 





