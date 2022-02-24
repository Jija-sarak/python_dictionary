
a = [
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
j = []
# # [2', '7', '9', '5', '1'] 

for i in range(len (a)):
    for l in a[i]:
        if a[i][l] not in j:
             j.append(a[i][l])
print(j)
