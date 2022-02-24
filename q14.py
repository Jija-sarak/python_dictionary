# Q14.Write a Python program to multiply all the items in a dictionary.
k = int(input("enter a number of keys:"))
j = {}
i = 0
while i < k :
    key = input("enter a key :")
    value = int(input("enter a value:"))
    j[key] = value
    i+=1
print(j)
for a in j:
    m = j[a]
    for s in j:
        if j[s]!= j[a]:
            m=m*j[s]
print(m)
            