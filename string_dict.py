str1=input("Enter any String:")
w=str1.split()
d={ }
for i in w:
    if i not in d:
        d[i]=w.count(i)
for i in d:
    print(i,"is ",d[i])










