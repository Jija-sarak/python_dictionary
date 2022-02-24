# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
data = {
    'j':550, 
    'k':158,
    'l':596,
    'm':678,
    'n':110, 
    'p':257
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