# list comprehension
# [expression : loop : condition]
# birthyear = [2001,2002,2003,2004]
# ages = []
# for i in birthyear:
#     f = 2024 - i
#     ages.append(f)
# print(ages)

# f = [2024 - i for i in birthyear ]
# print(f) 

# deposit = [ 50,100,200,300,400]
# above100 = []
# for i in deposit:
#     if(i > 100):
#         above100.append(i)
# print(above100)

# e = [i  for i in deposit if i > 100]
# print(e)

listD = [88,65,98,73,31,99,66]
oddeven = []
# for i in listD:
#     if i % 2 == 0:
#         oddeven.append("even")
#     else:
#         oddeven.append("odd")
# print(oddeven)

f = ["even" if i % 2 == 0 else "odd" for i in listD]
print(f)




