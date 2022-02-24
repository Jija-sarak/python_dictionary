# Q40. Write a Python program to convert more than one list to nested dictionary. 

# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
j = ['S001', 'S002', 'S003', 'S004']
a = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
s = [85, 98, 89, 92]
r = []
i = 0 
while i < len(j):
    k = 0
    n = {}
    m = {}
    while k < 2:
       m[a[i]] = s[i]
       k+=1
    n[j[i]]=m
    i+=1
    r.append(n)
print(r)