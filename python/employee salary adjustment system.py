emp = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]
l=[]
print("original dictionary",emp)
def change(d):
    if d["rating"]==4 or d["rating"]==5:
        x=lambda k: k+(10/100)*k
        d["salary"]=x(d["salary"])
        l.append(d)
    elif d["rating"]==3:
        x=lambda k: k+(5/100)*k
        d["salary"]=x(d["salary"])
        l.append(d)
    else:
        x=lambda k: k-(3/100)*k
        d["salary"]=x(d["salary"])
        l.append(d)

x=list(map(change,emp))
print("updated dictionary",l)
