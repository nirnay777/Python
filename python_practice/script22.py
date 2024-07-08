#int as param and inte as a return type
# def add(x,y):
#     return x + y
# r = add(7,3)
# print(r)

#float as paramter and float as return type
# def add(x,y):
#     return x + y
# t = add(23.6,8.9)
# print(t)

#string as paramter and string as return type
# def greet(name):
#     return "hello" +name
# e = greet("nirnay")
# print(e)


#boolean as paramter and boolean as return type
# def canvote(above18):
#     if above18:
#         return  True
#     else:
#         False
# e = canvote(False)
# if(e):
#     print("allowed to vote")
# else:
#     print("not allowed to vote")


#list as param and list as return type
# city = ["chandigarh","shimla","dehradun"]
# def addcity(lst):
#     lst.append("nagpur")
#     return lst
# e = addcity(city)
# print(e)
# print(city)

#dict as param and dict as return type
# dict = {
#     "firstname":"nirnay",
#     "lastname":"sangolkar"
# }

# def addCityToInfo(info):
#     info['city'] = "mumbai"
#     return info
# f =addCityToInfo(dict)
# print(f)

#tuple as param and tuple as return type

# def addNum(tupA):
#     tupA = list(tupA)
#     tupA.append(666)
#     tupA = tuple(tupA)
#     return tupA
# a,b,c = addNum((2,3))
# print(a)
# print(b)
# print(c)

#set as param and set as return type

setA = {11,33,55}
def addToSetA(ss):
    ss.add(44)
    return ss
f = addToSetA(setA)
print(setA)