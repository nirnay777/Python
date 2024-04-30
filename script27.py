# f = open('myfile.txt','w')
# str = input('enter the name')
# f.write(str)
# f.close

# f = None
# try:
#     fileName = input('enter the filename')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("file not found")
# finally:
#     if f is not None:
#         f.close()
# print("bye")


# f = open("myfile2.txt",'w')
# name = input('enter the name')
# f.write(name)
# f.close()


# fileName = input('please enter the fileName')
# f = open(fileName,'r')
# print(f.read())

# f.close

# f = None
# try:
#     fileName = input('please enter the filename')
#     f = open(fileName, 'r')
#     str = f.read()
#     print(str)
# except FileNotFoundError:
#     print("file not found")
# finally:
#     if f is not None:
#         f.close()

# f = open('myfile3.txt',"w")
# while str != "@":
#     str = input('enter the name'+'\n')
#     if str != "@":
#         f.write(str + '\n')
# f.close()

# f = open('myfile2.txt','a+')
# while str != "@":
#     str = input("enter the names")
#     if str != '@':
#         f.write(str + "\n")
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close()


import os , sys
fname = input('enter the filename:')
if os.path.isfile(fname):
    f = open(fname,'r')
else:
    sys.exit()
print('the file contents are:')
str = f.read()
print(str)
f.close()

# fname = input('enter the filename:')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     print("file does not exist")
#     sys.exit()



cc = 0
cw = 0
cl = 0

for line in f:
    cl = cl + 1
    list = line.split()
    cw = cw + len(list)
    cc = cc + len(line)
print(cl)
print(cw)
print(cc)





