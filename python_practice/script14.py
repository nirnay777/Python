fruit = "watermelon"
print("a" in fruit)
print("A" in fruit)

for i in  range(len(fruit)):
    print(i)
    print(fruit[i])

for i in fruit :
    print(i)


country = "Brazil"
e = len(country)
print(e)

t1 = country.upper()
print(t1)

t2 = country.lower()
print(t2)

t3 = country.capitalize()
print(t3)


t4 = country.startswith("B")
t5 = country.endswith("il")
print(t4)
print(t5)


info = " i am the worst"
t6 = info.replace("worst","best")
print(t6)

info = [ "nirnay","sangolkar","7263880368"]
t7 = '@'.join(info)
print(t7)