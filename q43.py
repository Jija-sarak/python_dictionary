# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
j = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
a = []
for i in j :
    for k in j:
        m =0
        while m<len(j[k]):
            if i!=j and i!=k:
               a.append({i:j[i][m],k:j[k][m]})
            m+=1
    break
print(a)