import numpy as np
from numpy import random
s=random.randint(1,100,size=(6,3))
print(s)
k=np.sum(s,axis=0)
print("total resources needed(tons):",end="")
d={}
d["oxygen"]=int(k[0])
d["water"]=int(k[1])
d["food"]=int(k[2])
print(d)
for i in range(6):
  a=np.max(s[i])
  if i==0:
    print("oxygen:",end="")
  elif i==1:
    print("water:",end="")
  else:
    print("food:",end="")
  print(np.max(s[i]))
print("transposed matrix:",end="")
l=[]
for i in range(3):
  b=[]
  for j in range(6):
    b.append(int(s[j][i]))
  l.append(b)
print(l)


