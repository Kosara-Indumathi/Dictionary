str1=input("Enter any String:")
d={ }
for i in str1:
    if i not in d:
        d[i]=str1.count(i)
for i in d:
    print(d[i])