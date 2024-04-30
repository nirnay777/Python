letters = ("S","A","N","S")
print(letters)
print(type(letters))
print(len(letters))
b = list[letters]
print(b)

# for i in letters:
#     print(i)



setA = {"22,44,55"}
print(type(setA))

setB ={22,33,44,55,66,77,77}
setB.add(88)
print(setB)

# print(setB)
# print(len(setB))

# print(setB[0])   #does not store value by index


setB.pop()
print(setB)          #doesn't take argument


setB.remove(77)
print(setB)