lst = [2000,2001,2002,2003]
ages = []
for x in lst:
    ages.append(2024 - x)
print(ages)


a = [2024 - x for x in lst]               #expression-loop condition
print(a)


number = [4,6,8,10,13]
c = [x * x for x in number]
print(c)

d = [x for x in number if x % 2 == 0]
print(d)

e = ['even' if x % 2 == 0 else "odd" for x in number]
print(e)

phones = ["iphone","redmi","samsung", "googlepixel"]
f = ["Mr/Mrs" + x for x in phones if len(x) > 5]
print(f)



