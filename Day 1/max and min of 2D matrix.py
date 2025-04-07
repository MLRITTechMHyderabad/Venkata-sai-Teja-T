maximum=[]
minimum=[]
for i in range(2):
    a=list(map(int,input().split()))
    maximum.append(max(a))
    minimum.append(min(a))
print("maximum value is",max(maximum))
print("minimum value is",min(minimum))