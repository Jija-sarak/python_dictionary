# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary:  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
j=  {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
s = {}
for i in j:
    k = 0
    sum=""
    while k<len(i):
        if i[k]!= " ":
            sum+=i[k]
        k+=1
    s[sum]=j[i]
print(s)


