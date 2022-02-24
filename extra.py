string = [1,1,2,3,2,2,4,5,4,4]
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


