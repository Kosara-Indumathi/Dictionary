a={1:2,3:4,4:3,2:1,0:0}
for i in a:
    d=sorted(a.items())
print("ascending order:",d)
d.sort(reverse=True)
print("descending order:",d)
print(dict(d))



