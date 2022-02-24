# Q 1
# details={
#     "name":"Shanti",
#     "age":12,
#     "email":"shanti@navgurukul.org",
#     }

# print(details["name"])
# print(details["name"])
# print(details["age"])

# Q 2
# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1:    
#     sum=sum+ dict1[i]
# print(sum)

#   Q 3
# c=dict()
# for i in range(1,16):
#     c[i]=i*i
# print(c) 

# Q 4
s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
a={'python':20,"gaurav":300,'dev':34,"karan":43}
c={}
for i in (s,a):
    c.update(i)
print(c)