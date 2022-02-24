# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
data =  {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max = 0
for i in data :
    if data[i]>max:
        max=data[i]
        s = i
print(s, max)
second_max = 0
for i in data:
    if data[i]>second_max:
        if data[i]!=max :
            second_max= data[i]
            s = i
print(s,second_max)
third_max = 0
for i in data:
    if data[i]> third_max:
        if data[i]!=max and data[i]!= second_max :
            third_max= data[i]
            s = i
print(s,third_max)