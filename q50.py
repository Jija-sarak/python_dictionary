# Q51.Write a Python program to filter even numbers from a given dictionary values. 
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}

# a = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
a = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
for i in a :
    j = 0
    b = []
    c = []
    while j<len(a[i]):
        if a[i][j]%2==0:
            b.append(a[i][j])
        else:
            c.append(a[i][j])
        j+=1
    a[i]=b
print(a)
