# def word(user):
#     count={}
#     for i in user:
#         count[i]=user.count(i)
#     return count
# user=input("enter the string:")
# print(word(user))




import json
def function(list):
    a={}
    for i in range(len(list)-1):
       b={list[i]:list[i+1]}
       a.update(b)
    print(a)
function([1,2,3,4,5])