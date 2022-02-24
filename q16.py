# Q16.Write a Python program to map two lists into a dictionary.
a = int(input("enter a number:"))
b = []
c = []
i = 0
while i<a:
    d = input("enter a key:")
    b.append(d)
    e = input("enter a value:")
    c.append(e)
    i+=1
f = dict(zip(b,c))
print(f)
