# Q53.
# Write a Python program to convert a given list of lists to a dictionary. 
# Original list of lists:
# [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# {1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
a = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], 
[4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
j={}
i = 0
while i < len(a):
    k = 0
    l = []
    while k<len(a[i]):
        if k != 0:
            l.append(a[i][k])
        k+=1
    j[a[i][0]]=l
    i+=1
print(j)
