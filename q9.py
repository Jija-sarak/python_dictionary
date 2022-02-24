# Q9.Write a Python program to iterate over dictionaries using for loops.
k = int(input("enter a number:"))
j = {}
i = 0
while i < k:
    b = input("enter a key:")
    c = input("enter a value:")
    j[b]=c
    i+=1
print(j)
for a in j :
    print(a,j[a])
    