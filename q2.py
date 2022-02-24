# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
string = 'w3resource'
d = {}
i = 0
while i < len(string):
    j = 0
    c = 0
    while j < len(string):
        if string[i]==string[j]:
            c+=1
        j+=1
        d[string[i]] = c
    i+=1
print(d)




