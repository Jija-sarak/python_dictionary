# Q36.Write a Python program to match key values in two dictionaries. 
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
j = {'key1': 1, 'key2': 3, 'key3': 2} 
a = {'key1': 1, 'key2': 2}
for x , y in j.items() :
    for i , k in a.items():
        if x==i and y==k:
            print(x,":",y ,"is present in both j and a")

