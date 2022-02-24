# Q52. Write a Python program to find the specified number of maximum values in a given dictionary.
# Original Dictionary:
# {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:
# ['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']
A= {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
a= []
for i in A:
    a.append(A[i])
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]>a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
J = []
c=0
for j in range(len(a)):
        for i in A:
            if a[j]==A[i]:
                if c<5:
                    if i not in J: 
                        J.append(i)
                        c+=1
print(J)

