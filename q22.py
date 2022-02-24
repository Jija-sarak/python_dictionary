# Q22. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
data = {'1':['a','b'],'2':['c','d']}
a = []
for i in data :
    a.append(data[i])
j =0
c=0
k = 1
while j < len(a):
    h = 0
    while h < len(a[j]):
        print(a[c][j]+a[k][h])
        h+=1
    j+=1

