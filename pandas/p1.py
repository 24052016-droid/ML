import  pandas as pd 
s=pd.Series([10,20,30])
print(s)#one dimensional also starting from index 0 
data={"name":["anna","bob"],"age":[20,30]}
df=pd.DataFrame(data)
print(df)#2 dimensional also starting from index 0 
data={"name":["a","b","c"],"age":[20,40,30],"score":[1,2,3]}
df=pd.DataFrame(data)
print(df)