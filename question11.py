my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
for i in my_dict:
    for j in my_dict:
        if my_dict[i]<my_dict[j]:
            print(my_dict[j])
    break 