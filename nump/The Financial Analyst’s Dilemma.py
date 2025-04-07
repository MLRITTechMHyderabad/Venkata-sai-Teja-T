import numpy as np
from numpy import random
s=random.randint(100,500,size=(30,5))
print(s)
print(np.mean(s,axis=0))
print(np.max(s))
for i in range(30):
  for j in range(5):
    if s[i][j]==np.max(s):
      print(f"highest price recorded: {np.max(s)} at day {i}, company {j+1}")
mi=np.min(s)
print(mi)
ma=np.max(s)
normalized_prices=(s-mi)/(ma-mi)
print(normalized_prices)
for i in range(30):
  l=[]
  for j in range(5):
    if s[i][j]<200:
      l.append(s[i][j])
  if len(l)>0:
    print(f"risk investment days: day {i}:{l}")


