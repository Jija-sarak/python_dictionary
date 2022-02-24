# Q18.Write a Python program to get the maximum and minimum value in a dictionary.
data = {
    'a':50, 
    'b':58,
    'c':56,
    'd':10,
    'e':100, 
    'f':120
    }
s = 0
for i in data :
    s = data[i]
    for j in data:
        if i!=j and s <data[j]:
            s = data[j]
    break
print(s)

