#single inheritence

# class Father:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
    
#     def displayName(self):
#         print(self.firstName + self.lastName)
    
# class Son(Father):
#     def __init__(self,fn,ln,sn):
#         super().__init__(fn,ln)
#         self.sname = sn
    
#     def displaySName(self):
#         print(self.sname + self.lastName)
        

# nirnay = Son("ravindra","sangolkar","nirnay")
# print(nirnay.firstName)
# print(nirnay.lastName)
# nirnay.displayName()
# nirnay.displaySName()



#multi-level inheritence


# class GrandFather:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
        
#     def displayGname(self):
#         print(self.firstName + self.lastName)
        
# class Father(GrandFather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fname = ffn
    
#     def displayFname(self):
#         print(self.fname + self.lastName)
        
# class Son(Father):
#     def __init__(self,fn,ln,ffn,ssn):
#         super().__init__(fn,ln,ffn)
#         self.sname = ssn
        
#     def displaySname(self):
#         print(self.sname + self.lastName)

# nirnayA = Son("annaji","sangolkar","ravindra","nirnay")

# print(nirnayA.firstName)
# print(nirnayA.lastName)
# print(nirnayA.fname)
# print(nirnayA.lastName)

# nirnayA.displayFname()
# nirnayA.displayGname()
# nirnayA.displaySname()


#heirarchical inheritence

# class Mother:
#     def __init__(self,fn,ln):
#         self.firstName = fn
#         self.lastName = ln
    
#     def displayMName(self):
#         print(self.firstName + self.lastName)

# class Son(Mother):
#     def __init__(self,fn,ln,ssn):
#         super().__init__(fn,ln)
#         self.sname = ssn
    
#     def displaySName(self):
#         print(self.sname + self.lastName)
        
# class SonB(Mother):
#     def __init__(self,fn,ln,ssn2):
#         super().__init__(fn,ln)
#         self.snameb = ssn2
        
#     def displaySNameB(self):
#         print(self.snameb + self.lastName)

# nirnay = Son("ratna","sangolkar","nirnay")
# pranay = SonB("ratna","sangolkar","pranay")

# print(nirnay.firstName)
# print(nirnay.lastName)
# print(nirnay.sname)
# nirnay.displayMName()


# print(pranay.firstName)
# rint(pranay.lastName)
# pranay.displaySNameB()



#Multiple inheritence

class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called..")
        self.firstName = fn
        self.lastName = ln
    
    def displayName(self):
        print(self.firstName + self.lastName)

class Father:
    def __init__(self,fn,ln):
        print("father constructor called...")
        self.firstName = fn
        self.lastName = ln
        
    def displayName(self):
        print(self.firstName + self.lastName)

class Son(Mother, Father):
    def __init__(self,fn,ln,ssn):
        super().__init__(fn,ln)
        self.sname = ssn
        

nirnay = Son("Ravindra","sangolkar","nirnay")
print(nirnay.firstName)
print(nirnay.lastName)
print(nirnay.sname)



 
    


        







        
        
    
    


