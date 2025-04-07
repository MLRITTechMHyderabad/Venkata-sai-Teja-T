n=int(input("enter number of rows"))
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
s=[]
print("original matrix is")
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j],end=" ")
    print()
for i in range(len(l[0])):
    k=[]
    for j in range(len(l)):
        k.append(l[j][i])
    s.append(k)
print("transpose matrix is ")
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j],end=" ")
    print()