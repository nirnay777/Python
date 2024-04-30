import re
# str = "man sun mop run"
# result = re.search(r'm\w\w',str)
# print(result.group())
# if result:
#     print(result.group())


# str2 = "moon teen soon mean lean clean screen"
# list2 = re.findall(r'm\w\w',str2)
# print(list2)

# str2 = "madrid is the king of ucl"
# q3 = re.match(r'm\w\w',str2)
# print(q3.group())
# if q3:
#     q3.group()

# import re
# str3 = "this ; is it : world's greatest ever"
# result = re.split(r'\W+',str3)
# print(result)



# str4 = "i am learnig javascriet and javascriet"
# q4 = re.sub(r"javascriet","javascript",str4)
# print(q4)


# import re
# str = 'an apple a day keeps doctor away'
# listA = re.findall(r'a[\w]*',str)
# listA = re.findall(r'\ba[\w]*',str)
# print(listA)

# import re 
# str = 'the  meeting will be conducted on 1st and 21st of this month'
# listB = re.findall(r'\b\d[\w]*',str)
# listB = re.findall(r'\b\d[\d]*',str)
# print(listB)

# str = "one two three four five six seven 8 9 10"
# listC = re.findall(r'\b\w{5}\b',str)
# print(listC)

# str = "one two three four five six seven aa 8 9 10"
# listD = re.findall(r'\b\w{3,5}\b',str)
# print(listD)


# str = "one two three four five six seven aa 8 9 10"
# listD = re.findall(r'\b\d{1,}\b',str)
# print(listD)


# str = "one two three four five six seven aa 8 9 10 two"
# listD = re.findall(r't[\w]*\Z',str)
# print(listD)


str = "three one two three four five six seven aa 8 9 10 two"
listD = re.findall(r'\At[\w]*',str)
print(listD)