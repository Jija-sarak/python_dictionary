# Q46.Write a Python program to convert string values of a given dictionary, into integer/float datatypes. Go to the editor
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]
a = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
i = 0
while i < len(a):
    for j in a[i]:
        a[i][j] = int(a[i][j])
    i+=1
print(a)