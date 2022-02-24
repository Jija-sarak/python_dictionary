# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.
a = int(input("enter a number of keys:"))
j = {}
i = 0
while i < a :
    key = input("enter a key :")
    value = input("enter a value:")
    j[key] = value
    i+=1
print(j)
b = input("enter a key :")
if b in j:
    print("exist")
else:
    print("not exist")
