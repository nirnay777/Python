import pickle
rb =  open('CR7.jpg','rb')
rb2 = open('CR7JR.jpg','wb')
bytes = rb.read()
rb2.write(bytes)
rb.close()
rb2.close()

#program 1
# with open('info4.txt','w') as f:
#     f.write("i am learning js")
#     f.write("i am learning python")

# with open('info.txt','r') as f2:
#     str = f2.read()
#     print(str)


# import pickle
# class Emp:
#     def __init__(self,fn,ln,email,age):
#         self.firstName = fn
#         self.lastName = ln
#         self.email = email
#         self.age = age
    
#     def displayDetails(self):
#         print(self.firstName)
#         print(self.lastName)
#         print(self.email)
#         print(self.age)


# f = open('student.dat','wb')
# n = int(input('enter the number of objects'))
# for x in range(n):
#     fn = input("enter firstName")
#     ln = input("enter lastName")
#     email = input("enter email")
#     age = input("enter age")
#     e = Emp(fn,ln,email,age)
#     pickle.dump(e,f)
# f.close()
