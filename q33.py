# Q33.Python: Print a dictionary line by line
# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}
# Sample Output:

# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 
students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
for i in students:
    print(i)
    for j ,k in students[i].items():
        print(j,':',k)