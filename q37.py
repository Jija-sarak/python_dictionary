# Q38.. Write a Python program to drop empty Items from a given Dictionary. 
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}
j = {'c1': 'Red', 'c2': 'Green', 'c3': None}
k = {}
for i in j:
    if j[i]!=None:
        k[i]=j[i]
print(k)

        