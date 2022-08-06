# Write a program to display the name of all the employees whose salary is more than 25000 from the following dictionary.
# emp={1:(“Amit”,25000),2:(“Suman”,30000),3:(“Ravi”,36000)}
# Format of data is given below :
# {Empid : (Empname, EmpSalary}

emp={1:('Amit',25000),2:('Suman',30000),3:('Ravi',36000)}
d=list(emp.values())
for i in d:
    if i[1]>25000:
        print(i[0])

