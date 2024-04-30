brands = ["leecooper","pepejeans","levis","gucci" ,"armani"]
# greater5 = []
# for x in brands:
#     if len(x) > 5:
#         greater5.append(x)
# print(greater5)

# print([x for x in brands if len(x) > 5])
# e = list(filter(lambda x : len(x) > 5, brands))
# print(e)

transactions = []
d = [8,9,10,-50,-60,88,77]
for x in d:
    if x < 0 :
        # print("withdrawl")
        transactions.append("withdraw")
    else:
        transactions.append("deposit")
# print(transactions)
# print(["withdrawl" if x < 0 else "deposit" for x in d])
# print(list(filter(lambda x : x > 0, d)))
# print(list(filter(lambda x : x < 0 , d)))

        




