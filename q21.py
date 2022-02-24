# Q21.Write a Python program to print all unique values in a dictionary. 

# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
j = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
        {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
a = []
i = 0
while i < len(j):
    for s in j[i]:
        if j[i][s] not in a:
          a.append(j[i][s]) 
    i+=1
print(a)