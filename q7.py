'''Q7.
Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for i in dic1:
    dic4[i] = dic1[i]
for j in dic2:
    dic4[j]=dic2[j]
for k in dic3:
    dic4[k]=dic3[k]
print(dic4)

