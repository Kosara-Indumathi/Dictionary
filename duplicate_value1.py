dict = {"V":"S001", "V": "S002", "VI": "S001", "VI": "S005", "VII":"S005", "V":"S009","VIII":"S007"}
a=[]
# b=dict(data)
for i in dict.values():
    if i in a :
        continue
    else:
        a.append(i)
print(a)
