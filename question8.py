# {
#     'sonu':85,
#     'Kartik':90,
#     'Deepak':96,
#     'Aman':76,
#     'Somesh':60,
#     'Umesh':85,
#     'Amarpal':70,
#     'Roshan':57,
#     'Riyaz':98,
#     'Shabid':56
# } 
# s = {}
# i = 0 
# while i < 10:
#     a = input("enter a student name:")
#     j = int(input("enter students marks:"))
#     s[a]=j
#     i+=1
# print(s)
h = int(input("enter a number:"))
s={}
for i in range(h):
    a = input("enter a student name:")
    j = int(input("enter student marks:"))
    s[a]=j
print(s)

