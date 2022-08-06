d1={1:"aman",2:"suman",3:"aman"}
a={}
for k,v in d1.items():
    if v not in a.values():
        a[k]=v
print(a)