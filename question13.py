data = {
    'a':50, 
    'b':58,
    'c':56,
    'd':40,
    'e':100, 
    'f':20
    }
max1 = []
max = 0
for i in data :
    if data[i]>max:
        max=data[i]
        s = i
max1.append(s)
second_max = 0
for i in data:
    if data[i]>second_max:
        if data[i]!=max :
            second_max= data[i]
            s = i
max1.append(s)
third_max = 0
for i in data:
    if data[i]> third_max:
        if data[i]!=max and data[i]!= second_max :
            third_max= data[i]
            s = i
max1.append(s)
print(max1)