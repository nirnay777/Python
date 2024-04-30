# #single inheritence

# class Son:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
        
#     def displayName(self):
#         print(self.firstName + self.lastName) 
        
# nirnay = Son("nirnay","sangolkar","777")
# print(nirnay.firstName)   
# print(nirnay.lastName)
# print(nirnay.adharNo)
# nirnay.displayName()

# class Father(Son):
#     salary = 100000
#     def displaySalary(self):
#         print(self.salary)

# Ravindra = Father("Ravindra","Sangolkar","135")
# print(Ravindra.firstName)
# print(Ravindra.lastName)
# print(Ravindra.adharNo)
# print(Ravindra.salary)
# Ravindra.displayName()
# Ravindra.displaySalary()

# class student:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
    
#     def displayName(self):
#         print(self.firstName + self.lastName)
        
# class Teacher(student):
#     def __init__(self,fn,ln,adharNo,salary):
#         super().__init__(fn,ln,adharNo)
#         self.salary = salary
        
#     def displaysalary(self):
#         print(self.salary)
        
# chinmayT = Teacher("chinmay","deshpande","456","500000")
# print(chinmayT.firstName)
# print(chinmayT.lastName)
# print(chinmayT.adharNo)
# print(chinmayT.salary)


# chinmayT.displayName()
# chinmayT.displaysalary()



# class Student:
#     def __init__(self,fn,ln,adharNo):
#         self.firstName = fn
#         self.lastName = ln
#         self.adharNo = adharNo
        
#     def displayName(self):
#         print(self.firstName + self.lastName)

# class Teacher(Student):
#     def __init__(self,fn,ln,adharNo,salary):
#         super().__init__(fn,ln,adharNo)
#         self.salary = salary
        
#     def displaySalary(self):
#         print(self.salary)
    
# class Professor(Teacher):
#     def __init__(self,fn,ln,adharNo,salary,spec):
#         super().__init__(fn,ln,adharNo,salary)
#         self.special = spec
                
#     def displaySpecialization(self):
#         print(self.special)

# sanjay = Professor("sanjay","zade",345,"50000","maths")
# print(sanjay.firstName)
# print(sanjay.lastName)
# print(sanjay.adharNo)
# print(sanjay.salary)
# print(sanjay.special)



# sanjay.displayName()
# sanjay.displaySalary()
# sanjay.displaySpecialization()


        


















    
    
