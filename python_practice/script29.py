# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln 

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher:
#     def __init__(self,fn,ln,salary):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.salary = salary
    
#     def displayName(self):
#         print(self.firstName + self.lastName)

#     def displaySalary(self):
#         print(self.salary)


# Ravindra = Student("Ravindra","Sangolkar")
# print(Ravindra.firstName)
# print(RavindralastName)
# Ravindra.displayName()




# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName + self.lastName)


# class Teacher(Student):
#     salary = 10000
#     def displaySalary(self):
#         print(self.salary)

# sarika = Teacher("sarika","pansare")
# print(sarika.firstName)
# print(sarika.lastName)
# print(sarika.salary)

# sarika.displayName()
# sarika.displaySalary()




# class Student:
#     def __init__(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln 

#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     def __init__(self, fn, ln,sl):
#         super().__init__(fn,ln)
#         self.salary = sl
    
#     def displaySalary(self):
#         print(self.salary)

# nirnay = Teacher("nirnay","sangolkar",1000)

# print(nirnay.firstName)
# print(nirnay.lastName)
# nirnay.displayName()
# nirnay.displaySalary()
        
class  GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn
    def displaySName(self):
        print(self.sname + self.lastName)

nirnay = Son("annaji","sangolkar","ravindra","nirnay")
print(nirnay.firstName)
print(nirnay.lastName)
print(nirnay.sname)

nirnay.displayFName()
nirnay.displayName()
nirnay.displaySName()

