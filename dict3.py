a="aaaabbbcccabcdeff"
i=0
while i<len(a)-1:
    if a[i]!=a[i+1]:
        print(a[i],end="")
    i+=1
print(a[-1])