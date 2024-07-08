# lambda functions

# add = lambda a,b:a+b
# e = add(1,9)
# print(e)

# sqr = lambda x : x * x
# r =sqr(4)
# print(r)


#positional arguments
# def sub(x,y):
#     return x-y
# r = sub(y =90 , x =45)
# print(r)

#*args
# def add(*args):
#     print(args)
#     total = 0
#     for i in args:
#         total = total + i
#     return total
# t = add(350,7,8,9,4,5,3,6,8,7,5,3,2,4)
# print(t)

#kwargs

def info(**kwargs):
    print(kwargs)
    kwargs['city'] = "nagpur"
    return kwargs
r = info(name = "nirnay", age ="34", roll= 69)
print(r)
