l=list(map(int,input().split()))
s=list(set(l))
d={}
for i in s:
    d[i]=l.count(i)
print(d)