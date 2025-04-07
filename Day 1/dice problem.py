
#dice problem
r=int(input("enter the r value:"))
a=[]
player1=player2=0
for i in range(1,7):
    for j in range(1,7):
        a.append([i,j])
print(a)
k={}

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
