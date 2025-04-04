cust = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]
def change(d):
    if d["age"]>40:
        return 0
    else:
        return 1
x=list(filter(change,cust))
def add_discount(d):
    if d["age"]>18 and d["age"]<26:
        a=lambda b:b-(10/100)*b
        d["total_purchase"]= a(d["total_purchase"])
        return d
    if d["age"]>25 and d["age"]<41:
        a=lambda b:b-(5/100)*b
        d["total_purchase"]= a(d["total_purchase"])
        return d
k=list(map(add_discount,x))
print(k)