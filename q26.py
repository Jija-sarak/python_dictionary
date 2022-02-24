# Q26.
# Write a Python program to print a dictionary in table format.
# my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# Sample Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in my_dict:
#     print(i , end=" ")
#     for k in my_dict[i]:
#         print(k,end=" ")
#     print()
for i in my_dict:
    print(i , end=" ")
for k ,n in my_dict.items() :
    if n == list:
        j = 0
        while j<len(n):
            print(n[j])
            j+=1
print()