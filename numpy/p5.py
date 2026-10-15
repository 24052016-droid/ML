import numpy as np 
a=np.array([[1],[2],[3]])
b=np.array([4,5,6])
print(a+b)# braodcasting 
# reshaping 
a=np.array([[1,2,],[3,4],[5,6]])
print(a.reshape(2,3))
print(a.flatten())