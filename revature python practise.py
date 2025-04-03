#transpose of a matrix
'''n=int(input("enter number of rows"))
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
    print()'''
















#max and min of 2D matrix

'''maximum=[]
minimum=[]
for i in range(2):
    a=list(map(int,input().split()))
    maximum.append(max(a))
    minimum.append(min(a))
print("maximum value is",max(maximum))
print("minimum value is",min(minimum))

    
#frequency of numbers in list
l=list(map(int,input().split()))
s=list(set(l))
d={}
for i in s:
    d[i]=l.count(i)
print(d)'''




#merging 2 dictionaries
#dice problem
r=int(input("enter the r value:"))
a=[]
player1=player2=0
for i in range(1,7):
    for j in range(1,7):
        a.append([i,j])
print(a)
k={}

for i in range(2,13):
    c=0
    for j in range(len(a)):
        if sum(a[j])==i:
            c+=1
    k[i]=c/36
print(k)








for i in range(len(a)):
    if sum(a[i]) not in k:
        k[sum(a[i])]=1
    else:
        k[sum(a[i])]+=1

for i in range(r):
    a,b,c,d=map(int,input().split())

    if k[a+b]/36<k[c+d]/36:
        player1+=1
    else:
        player2+=1


        
if player1>player2:
    print("player1 wins")
elif player1<player2:
    print("player2 wins")
else:
    print("draw")














    

    

        
      


