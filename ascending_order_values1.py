a={"swathi":45,"indu":20,"likitha":35,"sai likitha":60,"nagamani":50,"anu":40,"manjusha":65}
b=sorted(a,key=a.get) 
d=[]
for i in b:
    c=(i,a[i])
    d.append(c)  
print(dict(d))                        