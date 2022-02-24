dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
dic4 = {}
for i in dic1:
    for j in dic2 :
        if i in dic2 :
            dic4[i] = dic1[i]+dic2[j]
            if i != j:
                dic4[j]=dic2[j]
        else:
            dic4[i]=dic1[i]
for l in dic3:
    if i in dic3:
        dic4[i]=dic1[i]+dic3[l]
        if j in dic3:
             dic4[j]=dic2[j]+dic3[l]
        else:
            dic4[l]=dic3[l]
    else:
        dic4[l]=dic3[l]
print(dic4)
        
# for i in dic1:
#     for j in dic2 :
#         for k in dic3:
#             if i in dic2 and i in dic3:
#                 dic4[i] = dic1[i]+dic2[i]+dic3[i]
#             elif i in dic2:
#                 dic4[i]=dic1[i]+dic2[i]
#             elif i in dic3:
#                 dic4[i] = dic1[i]+dic3[i]
#             else:
#                 dic4[i] = dic1[i]
#                 dic4[j] = dic2[j]
#                 dic4[k] = dic3[k]
# print(dic4)
        



            

