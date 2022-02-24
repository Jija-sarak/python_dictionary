c = "MISSISSIPPI"
l = {}
i = 0
while i < len(c):
    j = 0
    count = 0
    while j<len(c):
        if c[i]==c[j]:
            count+=1
        j+=1
    l[c[i]]=count
    i+=1
print(l)

