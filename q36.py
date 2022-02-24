# Q37.Write a Python program to create a dictionary of keys x, y, and z 
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively. 
# Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# x has value [11, 12, 13, 14, 15, 16, 17, 18, 19]
# y has value [21, 22, 23, 24, 25, 26, 27, 28, 29]
# z has value [31, 32, 33, 34, 35, 36, 37, 38, 39]
A = {}

number_keys = int(input("enter a number :"))
i = 0
while i < number_keys:
    key = input("enter a key :")
    first_element = int(input("enter a element :"))
    c = first_element+9
    b = []
    while first_element < c:
        b.append(first_element)
        first_element+=1
    A[key]=b
    i+=1
print(A)
index = int(input("enter a number :"))
for i in A:
    j = 0
    while j < len(A[i]):
        if j == index-1:
            print(A[i][j])
        j+=1


