# class Person:
#     fn = "nirnay"
#     ln = "sangolkar"

#     def displayName(self):
#         print(self.fn + self.ln)

# nirnay = Person()
# vedant = Person()

# nirnay.displayName()
# vedant.displayName()
# vedant.fn = "vedant"
# vedant.ln = "gaikwad"
# vedant.displayName()


# class PersonB():
#     def __init__(self,fn,ln):
#         self.fn = fn 
#         self.ln = ln

#     def displayName(self):
#         print(self.fn + self.ln)

# Mithilesh = PersonB("Mithilesh","badge")
# Mithilesh.displayName()
# Sushant = PersonB("sushant","Bopche")
# Sushant.displayName()

# class PersonC:

#     def setFn(self,fn):
#         self.fn = fn 
#     def getFn(self):
#         return self.fn
    
#     def setLn(self,ln):
#         self.ln = ln

#     def displayName(self):
#         print(self.fn + self.ln)

# nirnay = PersonC()
# nirnay.setFn('Nirnay')
# nirnay.setLn('Sangolkar')

class PersonD:
    country = "india"
    def __init__(self,fn,ln):
        self.fn = fn 
        self.ln = ln

    @classmethod
    def changeCountry(cls):
        cls.country = "bharat"
   
    def displayName(self):
        print(self.fn+self.ln)

pratik = PersonD("pratik","shende")
ajay= PersonD("ajay",'jawade')
raj= PersonD("raj",'gidwani')

print(pratik.country)
print(raj.country)
pratik.country = "bharat"
print(pratik.country)
print(raj.country)
print(ajay.country)

PersonD.changeCountry()
print(pratik.country)
print(ajay.country)
print(raj.country)
