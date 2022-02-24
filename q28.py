# Q28.Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}
num_list = [1, 2, 3, 4]
new_dict = dict = {}
for num in num_list:
    dict[num] = {}
    dict = dict[num]
print(new_dict)
 