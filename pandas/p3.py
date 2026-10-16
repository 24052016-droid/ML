import pandas as pd
df1=pd.DataFrame({'id':[1,2],'name':["a",'b']})
df2=pd.DataFrame({'id':[1,2],'score':[90,80]})
merged=pd.merge(df1,df2,on="id")
print(merged)
df=pd.read_csv('files.csv')#for ectracting from the file
df.to_csv("files.csv",index=False)#for writing on to flie